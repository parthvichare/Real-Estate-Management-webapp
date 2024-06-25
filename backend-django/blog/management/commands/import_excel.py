# import_excel.py
import pandas as pd
from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Import data from Excel file into the database'

    def handle(self, *args, **kwargs):
        # Replace 'your_file.xlsx' with the path to your Excel file
        # excel_path = 'C:/Users/SIDDESH VICHARE/Downloads/Django development/backend-django/blog/management/commands/Backend_excel/flats.csv'
        excel_path= 'C:/Users/SIDDESH VICHARE/Downloads/Django development/backend-django/blog/templates/blog/flats.csv'
        df = pd.read_csv(excel_path)

        # Iterate over each row in the DataFrame
        for _, row in df.iterrows():
            # Create a new Person object and save it to the database
            person = Post(
                property_id=row['property_id'],
                name = row['title'],
                price = row['price'],
                Image_url = row['image_url'],
                beds = row['Beds'],
                floor=row['floor'],
                area_sqft=row['area_sqft'],
                super_areas=row['area'],
                furnishing=row['furnishing']
            )
            person.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
