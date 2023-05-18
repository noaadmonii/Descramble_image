import PIL as pil
import pandas as pd
import sqlite3 as db

from PIL import Image, ImageFilter



class Descramle:

    def __init__(self, img, tile_size):
       
       self.scrambled_img = Image.open(img)
       self.descrambled_img = Image.new('RGB', (self.scrambled_img.width , self.scrambled_img.height))
       self.tile_size = tile_size

       #show the original scrambled image I recieved
       self.scrambled_img.show()

        #connecting to the DB
       self.conn = db.connect("./assignment/assignment.sqlite")
       #self.cursor = self.conn.cursor() - commented since I'm not editing
       self.transformations = pd.read_sql_query('select * from transform', self.conn)
       self.df = pd.DataFrame(self.transformations)


    #add tile to the new image (the descrambled image)
    def concat(self, tile, x, y):
        self.descrambled_img.paste(tile, (x, y))
       
    
    #iterate over the DB while bringing tiles back to place
    def iterateSQL(self):
        for index, row in self.df.iterrows():
            dst_left = row["dst_tile_width"]*self.tile_size
            dst_top = row["dst_tile_height"]*self.tile_size
            tile = self.scrambled_img.crop((dst_left, dst_top, dst_left+self.tile_size, dst_top+self.tile_size))
            
            if row["direction"] == "clockwise":
                tile = tile.rotate(270)
            elif row["direction"] == "counterclockwise":
                tile = tile.rotate(90)
            
            
            src_left = row["src_tile_width"]*self.tile_size
            src_top = row["src_tile_height"]*self.tile_size
            self.concat(tile, src_left, src_top)
        
        #show descrambled image
        self.descrambled_img.show()
        #show descrambled image, but now, a blurred version, since this way the lines around each tile are less visible
        self.descrambled_img.filter(ImageFilter.GaussianBlur(2)).show()
        """"
        self.descrambled_img_blurred = self.descrambled_img.filter(ImageFilter.GaussianBlur(2))

        self.descrambled_img = self.descrambled_img.save("descrambled_img.jpg")
        self.descrambled_img_blurred = self.descrambled_img_blurred.save("descrambled_img_blurred.jpg")
        """

           
        

if __name__ == "__main__":
    des = Descramle("./assignment/assignment.jpg", 43)
    des.iterateSQL()
  
    