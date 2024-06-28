# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# import pandas as pd

# class PropertyScraperPipeline:
#     def __init__(self):
#         self.df_list = []  # Initialize an empty list to store DataFrames

#     def close_spider(self, spider):
#         # Concatenate all DataFrames in df_list
#         if self.df_list:
#             final_df = pd.concat(self.df_list, ignore_index=True)
#             # Save the concatenated DataFrame to an Excel file
#             final_df.to_excel('scraped_data.xlsx', index=False)

#     def process_item(self, item, spider):
#         # Convert the item to a DataFrame
#         df = pd.DataFrame([dict(item)])  # Create a DataFrame with a single row for the item
#         self.df_list.append(df)  # Append the DataFrame to df_list
#         return item

# In your scrapy project, create a new pipeline.py or modify an existing one

import mysql.connector
from itemadapter import ItemAdapter
import pandas as pd

class PropertyScraperPipeline:
    def __init__(self, db_user, db_password, db_host, db_name):
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name
        self.items = []  # List to accumulate scraped items

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
           db_user=crawler.settings.get('MYSQL_USER'),
           db_password=crawler.settings.get('MYSQL_PASSWORD'),
           db_host=crawler.settings.get('MYSQL_HOST'),
           db_name=crawler.settings.get('MYSQL_NAME')
        )

    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            database=self.db_name
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()
        self.save_to_excel()

    def save_to_excel(self):
        if self.items:
            # Convert the list of items to a DataFrame
            df = pd.DataFrame(self.items)
            
            # Save the DataFrame to an Excel file
            df.to_excel('flats.xlsx', index=False)
            print("Saved scraped data to scraped_data.xlsx")

    def process_item(self, item, spider):
        sql = """
            INSERT INTO flats (
                property_id, Landmark, title, price, area_sqft,
                property_name, image_url, carpet_area, super_area, status,
                furnishing, facing, floor, overlook, url, latitude, longitude,
                addressLocality, addressRegion, Beds, bathroom, balcony,
                parking, amenities, NearbyLocality, rating
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            item.get('property_id'),
            item.get('Landmark'),
            item.get('title'),
            item.get('price'),
            item.get('area_sqft'),
            item.get('property_name'),
            item.get('image_url'),
            item.get('carpet_area'),
            item.get('super_area'),
            item.get('status'),
            item.get('furnishing'),
            item.get('facing'),
            item.get('floor'),
            item.get('overlook'),
            item.get('url'),
            item.get('latitude'),
            item.get('longitude'),
            item.get('addressLocality'),
            item.get('addressRegion'),
            item.get('Beds'),
            item.get('bathroom'),
            item.get('balcony'),
            item.get('parking'),
            ', '.join(item.get('amenities', [])),  # Join list of amenities to string
            ', '.join(item.get('NearbyLocality', [])),  # Join list of NearbyLocality to string
            ', '.join(item.get('rating', []))  # Join list of ratings to string
        )
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            self.items.append(ItemAdapter(item).asdict())  # Append processed item to items list
        except mysql.connector.Error as err:
            print("Error:", err)
            self.conn.rollback()
        
        return item