import telegram.ext

Inventory_list = {}
weight_list = {}
Token = "5907331637:AAGFsp-bvyRziEtYGDfF5aEPRNRKG7JihrQ"
price = []
updater = telegram.ext.Updater("5907331637:AAGFsp-bvyRziEtYGDfF5aEPRNRKG7JihrQ",use_context = True)
dispatcher = updater.dispatcher
import json

def start(update,context):
    update.message.reply_text("Hello,welcome to swetanshu_general_store")
    update.message.reply_text("Great to see you here")
    update.message.reply_text("Type /help here to see different items for purchasing")
    update.message.reply_text("To see all items present with us")
    update.message.reply_text("Whatever you want to buy,suppose you want to buy 10 packets of Parle-G Biscuits")
    update.message.reply_text("""
    
                      Type like this ->

                      /Cookies_family Parle-G_Biscuits 10
                      
                      """
                        )
    update.message.reply_text("To see the items orders ,select /showInventory")
    update.message.reply_text("To see the total price of the items you booked, select /TotalPrice")
    update.message.reply_text("To book the order ,select /book_order")
    update.message.reply_text("To place an additional order that is not on the general store,use /add_order")
    update.message.reply_text("""
    
          
            To choose home delivery or shop pickup option for the order ,use -> 
                            /delivery_options

                            
                            """)
    
    update.message.reply_text("You can check multiple discount offers using -> /discount_offers")
    update.message.reply_text("You can choose your delivery options as -> want the home delivery type -> home")
    update.message.reply_text("want to buy offline   type -> pickup")
    update.message.reply_text(
        """
        Are you sure you want to book  the order, say 
        Yes or No

        """
    )
    update.message.reply_text("""
    
    for booking order ,type as ->  
     /book_order yes
    
    """)





def help(update ,context):
    update.message.reply_text(
        """

        /start ->  Hello,welcome to swetanshu_general_store
        /help ->  You can type help always to see all the items collection in our general store
        /content -> About different items present in Swetanshu general store
        /Cookies_family -> We have multiple delicious cookies of wide varieties.
        /Cookies_names -> give the names of all the available cookies
        /HairCare_Products -> We have multiple HairCare Products of wide varieties 
        /HairCare_Products_name -> give the names of all the available HairCare_Products
        /Soap -> We have multiple Bathing soap products of wide varieties 
        /Soap_name -> give the names of all the available soap_products
        /FastFood_Products -> We have multiple FastFood Products of wide varieties 
        /FastFood_name -> give the names of all the available fastfood
        /Dried_Vegis -> We have multiple dried vegetables
        /Dried_Vegis_name -> give the names of all the available Dried_Vegis_name
        /Dry_Fruits -> We have multiple Dry Fruits
        /Dry_Fruits_name -> give the names of all the available dry_fruits_name
        /Flour -> We have different flour products available for you
        /Flour_name -> give the names of all the available flour_name
        /Amul -> We have different Amul products available for you
        /Amul_product_name -> give the names of all the available amul_product_name
        /DairyMilk_Chocolates -> We have different DairyMilk products available for you
        /DairyMilk_product_name -> give the names of all the available dairy_product_name
        /Stationary_products -> This will show you staionary items
        /Stationary_products_name -> This will show you staionary item name
        /TotalPrice_with_discount -> if want to check the total price of the items you purchase then use this
        /book_order -> If your are sure to book your order , type /book_order
        /showInventory -> Want to see the current purchased items ,their price and their weight ,click here
        /Inventory -> Show all items you have
        /add_order -> To place an additional order that is not on the general store
        /delivery_options -> You can choose your own order pickup style
        /discount_offers -> Check all the latest discount offers
        """
    )



cookies_quantity = {

    'Parle-G_Biscuit': 10,
    'Coconut': 120,
    'Cadbury_Oreo': 10,
    'Sunfeast_Cream_Biscuits': 10,
    'Coconut_Crunch_by_Priyagold': 50,
    'Unibic_Choco_Chip_Cookies': 10,
    'Anmol': 20,
    'Britannia_Marie_Gold': 20,
    'Patanjali': 40,
    'Butter_Cracker_by_Cremica': 20

}

cookies_price = {

    'Parle-G_Biscuit': 5,
    'Coconut': 10,
    'Cadbury_Oreo': 30,
    'Sunfeast_Cream_Biscuits': 10,
    'Coconut_Crunch_by_Priyagold': 50,
    'Unibic_Choco_Chip_Cookies': 20,
    'Anmol': 20,
    'Britannia_Marie_Gold': 20,
    'Patanjali': 40,
    'Butter_Cracker_by_Cremica': 120

}

cookies_weight_gms = {

    'Parle-G_Biscuit': 500,
    'Coconut': 100,
    'Cadbury_Oreo': 300,
    'Sunfeast_Cream_Biscuits': 100,
    'Coconut_Crunch_by_Priyagold': 500,
    'Unibic_Choco_Chip_Cookies': 200,
    'Anmol': 200,
    'Britannia_Marie_Gold': 200,
    'Patanjali': 400,
    'Butter_Cracker_by_Cremica': 120
}

haircare_quantity = {


 'Dove': 200,
 'Sunsilk': 300,
 'Pantene': 100,
 'Himalaya': 100,
 'Nyle': 200,
 'TRESemme': 200,
 'Clinic_Plus': 100,
 'Head_and_Shoulders': 250,
 'Fiama_Di_Wills': 50,
 'Patanjali_Kesh_Kanti': 100,
 'Dabur_Vatika': 100

}


haircare_price = {


 'Dove': 50,
 'Sunsilk': 200,
 'Pantene': 5,
 'Himalaya': 100,
 'Nyle': 200,
 'TRESemme': 200,
 'Clinic_Plus': 100,
 'Head_and_Shoulders': 20,
 'Fiama_Di_Wills': 5000,
 'Patanjali_Kesh_Kanti': 10,
 'Dabur_Vatika': 10

}


haircare_weight_ml = {


 'Dove': 500,
 'Sunsilk': 200,
 'Pantene': 50,
 'Himalaya': 100,
 'Nyle': 200,
 'TRESemme': 200,
 'Clinic_Plus': 100,
 'Head_and_Shoulders': 200,
 'Fiama_Di_Wills': 500,
 'Patanjali_Kesh_Kanti': 100,
 'Dabur_Vatika': 100

}




soap_quantity = {


 'Clinic_Plus_soap': 100,
 'Dove_soap': 50,
 'Sunsilk_soap': 200,
 'Head_and_Shoulders_soap': 20,
 'Pantene_soap': 5,
 'Himalaya_soap': 100,
 'Nyle_soap': 200,
 'Fiama_Di_Wills_soap': 5000,
 'TRESemme_soap': 200,
 'Patanjali_Kesh_Kanti_soap': 10,
 'Dabur_Vatika_soap': 10

}

soap_price = {


'Clinic_Plus_soap': 100,
 'Dove_soap': 50,
 'Sunsilk_soap': 200,
 'Head_and_Shoulders_soap': 20,
 'Pantene_soap': 5,
 'Himalaya_soap': 100,
 'Nyle_soap': 200,
 'Fiama_Di_Wills_soap': 5000,
 'TRESemme_soap': 200,
 'Patanjali_Kesh_Kanti_soap': 10,
 'Dabur_Vatika_soap': 10


}


soap_weight_gms = {


'Clinic_Plus_soap': 100,
 'Dove_soap': 50,
 'Sunsilk_soap': 200,
 'Head_and_Shoulders_soap': 200,
 'Pantene_soap': 50,
 'Himalaya_soap': 100,
 'Nyle_soap': 200,
 'Fiama_Di_Wills_soap': 50,
 'TRESemme_soap': 200,
 'Patanjali_Kesh_Kanti_soap': 100,
 'Dabur_Vatika_soap': 100

}


fastfood_quantity = {


 'MccNuggets': 50,
 'WAFFLE_FRIES_CHICK-FIL-A': 50,
 'DOUBLE-DOUBLE_Burger': 100,
 'French_Fries': 100,
 'CHICKEN_POPEYES': 200,
 'CHICKEN_SANDWICH': 40,
 'Curly_Fries': 100,
 'Blizzard_Ice_Cream': 50,
 'Frosty_Quuen_coke': 100,
 'Bacon_Cheese_burger': 89

}


fastfood_price = {


'MccNuggets': 50,
 'WAFFLE_FRIES_CHICK-FIL-A': 50,
 'DOUBLE-DOUBLE_Burger': 100,
 'French_Fries': 100,
 'CHICKEN_POPEYES': 200,
 'CHICKEN_SANDWICH': 40,
 'Curly_Fries': 100,
 'Blizzard_Ice_Cream': 50,
 'Frosty_Quuen_coke': 100,
 'Bacon_Cheese_burger': 89

}

fastfood_weight_gms = {


'MccNuggets': 500,
 'WAFFLE_FRIES_CHICK-FIL-A': 500,
 'DOUBLE-DOUBLE_Burger': 1000,
 'French_Fries': 1000,
 'CHICKEN_POPEYES': 2000,
 'CHICKEN_SANDWICH': 400,
 'Curly_Fries': 1000,
 'Blizzard_Ice_Cream': 500,
 'Frosty_Quuen_coke': 1000,
 'Bacon_Cheese_burger': 890

}




dried_vegis_quantity = {


 'Dehydrated_Onion': 122,
 'Dehydrated_Garlics': 112,
 'Dehydrated_Carrot_Flake': 31,
 'Dehydrated_Onion_Granule': 41,
 'Vegetable_&_Herb_Flakes': 14,
 'Dehydrated_Cabbage_Flake': 141,
 'Dehydrated_Beetroot': 144,
 'Vegetable_Granule': 41


}

dried_vegis_price = {


 'Dehydrated_Onion': 50,
 'Dehydrated_Garlics': 100,
 'Dehydrated_Carrot_Flake': 100,
 'Dehydrated_Onion_Granule': 100,
 'Vegetable_&_Herb_Flakes': 100,
 'Dehydrated_Cabbage_Flake': 100,
 'Dehydrated_Beetroot': 12,
 'Vegetable_Granule': 13


}

dried_vegis_weight_gms = {


 'Dehydrated_Onion': 100,
 'Dehydrated_Garlics': 122,
 'Dehydrated_Carrot_Flake': 310,
 'Dehydrated_Onion_Granule': 410,
 'Vegetable_&_Herb_Flakes': 140,
 'Dehydrated_Cabbage_Flake': 140,
 'Dehydrated_Beetroot': 144,
 'Vegetable_Granule': 410


}



dry_fruits_quantity = {

 'Pistachios_-_Pista': 124,
 'Apricot_-_Khubani': 121,
 'Dates_-_Khajoor': 23,
 'Cashew_-_Kaju': 123,
 'Almonds_-_Badam': 243,
 'Walnuts_-_Akhrot': 112,
 'Raisins_-_Kismis': 235,
 'Hazelnuts_-_Pahadi_Badam': 123,
 'Dry_Figs_-_Anjeer': 131,
 'Dry_Berries_-_Jamun': 231,
 'Fox_Nuts_-_Makhana': 123,
 'Seeds_-_Beej': 114

}


dry_fruits_price = {

 'Pistachios_-_Pista': 300,
 'Apricot_-_Khubani': 200,
 'Dates_-_Khajoor': 500,
 'Cashew_-_Kaju': 1000,
 'Almonds_-_Badam': 1000,
 'Walnuts_-_Akhrot': 1500,
 'Raisins_-_Kismis': 3000,
 'Hazelnuts_-_Pahadi_Badam': 4000,
 'Dry_Figs_-_Anjeer': 1000,
 'Dry_Berries_-_Jamun': 5000,
 'Fox_Nuts_-_Makhana': 1000,
 'Seeds_-_Beej': 100

}


dry_fruits_weight_gms = {

 'Pistachios_-_Pista': 300,
 'Apricot_-_Khubani': 200,
 'Dates_-_Khajoor': 500,
 'Cashew_-_Kaju': 100,
 'Almonds_-_Badam': 100,
 'Walnuts_-_Akhrot': 150,
 'Raisins_-_Kismis': 300,
 'Hazelnuts_-_Pahadi_Badam': 400,
 'Dry_Figs_-_Anjeer': 100,
 'Dry_Berries_-_Jamun': 500,
 'Fox_Nuts_-_Makhana': 100,
 'Seeds_-_Beej': 100

}



flour_quantity = {

 'JOWAR': 200,
 'WHOLE_WHEAT_FLOUR': 200,
 'BREAD_FLOUR': 100,
 'ALMOND_FLOUR': 300,
 'OAT_FLOUR': 200,
 'TAPIOCA_FLOUR': 300,
 'Rye_Flour': 100

}



flour_price = {

'JOWAR': 121,
 'WHOLE_WHEAT_FLOUR': 80,
 'BREAD_FLOUR': 150,
 'ALMOND_FLOUR': 124,
 'OAT_FLOUR': 142,
 'TAPIOCA_FLOUR': 214,
 'Rye_Flour': 90

}


flour_weight_gms = {

'JOWAR': 1210,
 'WHOLE_WHEAT_FLOUR': 800,
 'BREAD_FLOUR': 1500,
 'ALMOND_FLOUR': 1240,
 'OAT_FLOUR': 1420,
 'TAPIOCA_FLOUR': 240,
 'Rye_Flour': 900

}





amul_quantity = {

'Amul_Buttermilk': 100,
 'Amul_Lassi': 100,
 'Amul_Immunity_Shots': 30,
 'Amul_Tru': 200,
 'Amul_Cheese_Spread': 300,
 'Amul_Choco_Buttery_Spread': 300,
 'Amul_Dahi_Tikki': 100,
 'Amul_French_Fries': 10,
 'Amul_Paneer_Nuggets': 20,
 'Amul_Premium_Dahi': 300,
 'Amul_Fresh_Paneer': 300
    }


amul_price = {

'Amul_Buttermilk': 200,
 'Amul_Lassi': 10,
 'Amul_Immunity_Shots': 100,
 'Amul_Tru': 100,
 'Amul_Cheese_Spread': 200,
 'Amul_Choco_Buttery_Spread': 300,
 'Amul_Dahi_Tikki': 100,
 'Amul_French_Fries': 100,
 'Amul_Paneer_Nuggets': 200,
 'Amul_Premium_Dahi': 30,
 'Amul_Fresh_Paneer': 300

    }


amul_weight_gms = {

'Amul_Buttermilk': 200,
 'Amul_Lassi': 100,
 'Amul_Immunity_Shots': 100,
 'Amul_Tru': 100,
 'Amul_Cheese_Spread': 200,
 'Amul_Choco_Buttery_Spread': 300,
 'Amul_Dahi_Tikki': 100,
 'Amul_French_Fries': 100,
 'Amul_Paneer_Nuggets': 200,
 'Amul_Premium_Dahi': 300,
 'Amul_Fresh_Paneer': 300

    }




dairymilk_quantity = {

'Dairy_Milk_Freddo_Caramel': 100,
 'Dairy_Milk_Fruit_&_Nut': 100,
 'Dairy_Milk_Inventor_Bars_Banoffee_Nut_Crumble': 123,
 'Dairy_Milk_Inventor_Bars_Fizzing_Cherry': 124,
 'Dairy_Milk_Inventor_Bars_No_Frowny_Brownie': 23,
 'Dairy_Milk_Little_Bar': 1441,
 'Dairy_Milk_Madbury_Crunchy_Honeycomb': 142,
 'Dairy_Milk_Marvellous_Creations_Jelly_Popping_Candy': 142

}


dairymilk_price = {

 'Dairy_Milk_Freddo_Caramel': 1312,
 'Dairy_Milk_Fruit_&_Nut': 412,
 'Dairy_Milk_Inventor_Bars_Banoffee_Nut_Crumble': 412,
 'Dairy_Milk_Inventor_Bars_Fizzing_Cherry': 123,
 'Dairy_Milk_Inventor_Bars_No_Frowny_Brownie': 2231,
 'Dairy_Milk_Little_Bar': 114,
 'Dairy_Milk_Madbury_Crunchy_Honeycomb': 141,
 'Dairy_Milk_Marvellous_Creations_Jelly_Popping_Candy': 142

}



dairymilk_weight_gms = {

 'Dairy_Milk_Freddo_Caramel': 1320,
 'Dairy_Milk_Fruit_&_Nut': 420,
 'Dairy_Milk_Inventor_Bars_Banoffee_Nut_Crumble': 420,
 'Dairy_Milk_Inventor_Bars_Fizzing_Cherry': 120,
 'Dairy_Milk_Inventor_Bars_No_Frowny_Brownie': 231,
 'Dairy_Milk_Little_Bar': 1104,
 'Dairy_Milk_Madbury_Crunchy_Honeycomb': 1041,
 'Dairy_Milk_Marvellous_Creations_Jelly_Popping_Candy': 1042

}




Stationary_products_quantity = {

        "Staplers":100,
        "Punching_Machine":100,
        "Sticky_Tapes":100,
        "Scissors":100,
        "Glue":100,
        "Calculator":123,
        "Tape_Dispenser":1231,
        "Desk_Tidy":122,
        "Pen_Cups":1231,
        "Note_Holders":2014,
        "Paper_Clip":1224,
        "Waste_buckets":1411,

}




Stationary_products_price = {

        "Staplers":123,
        "Punching_Machine":131,
        "Sticky_Tapes":12,
        "Scissors":34,
        "Glue":13,
        "Calculator":1233,
        "Tape_Dispenser":1231,
        "Desk_Tidy":1212,
        "Pen_Cups":12,
        "Note_Holders":214,
        "Paper_Clip":124,
        "Waste_buckets":1411,

}

Stationary_products_weight_gms = {

        "Staplers":1203,
        "Punching_Machine":1301,
        "Sticky_Tapes":102,
        "Scissors":304,
        "Glue":130,
        "Calculator":133,
        "Tape_Dispenser":121,
        "Desk_Tidy":112,
        "Pen_Cups":120,
        "Note_Holders":210,
        "Paper_Clip":124,
        "Waste_buckets":111,

}




def content(update,context):
    update.message.reply_text(
        """
        We have varoius items in our general store,I will show you the items here :
        items = [Cookies,HairCare,Soap,FastFood,Dried Vegis, Dry Fruits, FLour,Amul,DairyMilk,Stationary_products]

        These are all the items available with us right now

        If you want something else apart from these, simple go to - 
        /add_orders -> enter the product details


        We will be having this item in future for you ,and we will call you after this.
        Thankyou so much 

        """
    )


def Cookies_names(update,context):
    

    wei = json.dumps(cookies_weight_gms)
    update.message.reply_text(wei)
    update.message.reply_text(
        """ 

        'Parle_-G_Biscuit',
 'Patanjali',
 'Butter_Cracker_by_Cremica',
 'Coconut',
 'Cadbury_Oreo',
 'Sunfeast_Cream_Biscuits',
 'Coconut_Crunch_by_Priyagold',
 'Unibic_Choco_Chip_Cookies',
 'Anmol',
 'Britannia_Marie_Gold

        """
            
    )
def HairCare_Products_name(update,context):



    wei = json.dumps(haircare_weight_ml)
    update.message.reply_text(wei)

    update.message.reply_text(
        """ 

'Clinic_Plus',
 'Dove',
 'Sunsilk',
 'Head_and_Shoulders',
 'Pantene',
 'Himalaya',
 'Nyle',
 'Fiama_Di_Wills',
 'TRESemme',
 'Patanjali_Kesh_Kanti',
 'Dabur_Vatika'


        """
            
    )


def Soap_name(update,context):

    wei = json.dumps(soap_weight_gms)
    update.message.reply_text(wei)

    update.message.reply_text(

        """ 

 'Clinic_Plus_soap',
 'Dove_soap',
 'Sunsilk_soap',
 'Head_and_Shoulders_soap',
 'Pantene_soap',
 'Himalaya_soap',
 'Nyle_soap',
 'Fiama_Di_Wills_soap',
 'TRESemme_soap',
 'Patanjali_Kesh_Kanti_soap',
 'Dabur_Vatika_soap'


        """
            
    )

def FastFood_name(update,context):

    wei = json.dumps(fastfood_weight_gms)
    update.message.reply_text(wei)

    update.message.reply_text(

        """ 

 'WAFFLE_FRIES_CHICK-FIL-A',
 'DOUBLE-DOUBLE_Burger',
 'French_Fries',
 'CHICKEN_POPEYES',
 'CHICKEN_SANDWICH',
 'Curly_Fries',
 'Blizzard_Ice_Cream',
 'Frosty_Quuen_coke',
 'Bacon_Cheese_burger',
 'MccNuggets'

        """
            
    )


def Dried_Vegis_name(update,context):

    wei = json.dumps(dried_vegis_weight_gms)
    update.message.reply_text(wei)

    update.message.reply_text(

        """ 

'Dehydrated_Onion',
 'Dehydrated_Garlics',
 'Dehydrated_Carrot_Flake',
 'Dehydrated_Onion_Granule',
 'Vegetable_&_Herb_Flakes',
 'Dehydrated_Cabbage_Flake',
 'Dehydrated_Beetroot',
 'Vegetable_Granule'

        """
            
    )



def Dry_Fruits_name(update,context):

    wei = json.dumps(dry_fruits_weight_gms)
    update.message.reply_text(wei)


    update.message.reply_text(

        """ 

 'Pistachios_-_Pista',
 'Apricot_-_Khubani',
 'Dates_-_Khajoor',
 'Cashew_-_Kaju',
 'Almonds_-_Badam',
 'Walnuts_-_Akhrot',
 'Raisins_-_Kismis',
 'Hazelnuts_-_Pahadi_Badam',
 'Dry_Figs_-_Anjeer',
 'Dry_Berries_-_Jamun',
 'Fox_Nuts_-_Makhana',
 'Seeds_-_Beej'

 
        """
            
    )


def Flour_name(update,context):

    wei = json.dumps(flour_weight_gms)
    update.message.reply_text(wei)


    update.message.reply_text(

        """ 

  'WHOLE_WHEAT_FLOUR',
 'BREAD_FLOUR',
 'ALMOND_FLOUR',
 'OAT_FLOUR',
 'TAPIOCA_FLOUR',
 'JOWAR',
 'Rye_Flour'

        
        """
            
    )


def Amul_product_name(update,context):
    
    wei = json.dumps(amul_weight_gms)
    update.message.reply_text(wei)


    update.message.reply_text(

        """ 

'Amul_Buttermilk',
 'Amul_Lassi',
 'Amul_Immunity_Shots',
 'Amul_Tru',
 'Amul_Cheese_Spread',
 'Amul_Choco_Buttery_Spread',
 'Amul_Dahi_Tikki',
 'Amul_French_Fries',
 'Amul_Paneer_Nuggets',
 'Amul_Premium_Dahi',
 'Amul_Fresh_Paneer'
        
        """
            
    )


def DairyMilk_product_name(update,context):

    wei = json.dumps(dairymilk_weight_gms)
    update.message.reply_text(wei)

    update.message.reply_text(

        """ 
  
 'Dairy_Milk_Freddo_Caramel',
 'Dairy_Milk_Fruit_&_Nut',
 'Dairy_Milk_Inventor_Bars_Banoffee_Nut_Crumble',
 'Dairy_Milk_Inventor_Bars_Fizzing_Cherry',
 'Dairy_Milk_Inventor_Bars_No_Frowny_Brownie',
 'Dairy_Milk_Little_Bar',
 'Dairy_Milk_Madbury_Crunchy_Honeycomb',
 'Dairy_Milk_Marvellous_Creations_Jelly_Popping_Candy'

        
        """
            
    )


def Stationary_products_name(update,context):

    wei = json.dumps(Stationary_products_weight_gms)
    update.message.reply_text(wei)


    update.message.reply_text(

        """ 
  
        Staplers
        Punching_Machine
        Sticky_Tapes
        Scissors
        Glue
        Calculator
        Tape_Dispenser
        Desk_Tidy
        Pen_Cups
        Note_Holders
        Paper_Clip
        Waste_buckets
        
        """
            
    )




def Inventory(update,message):
    update.message.reply_text(

        """

        Cookies , Haircare, 
        Soap, Fastfood , 
        Dried_vegis , Dry_fruits, 
        Flour,  Amul,
        Cadbury Products, Stationary Items
        
        
        """

    )

def SeeInventory(name,quantity,Inventory_list):
    if name not in Inventory_list:
        Inventory_list[name] = int(quantity)
    else:
        Inventory_list[name] += int(quantity)



def Total_weight(name,weight,weight_list):
    if name not in weight_list:
        weight_list[name] = int(weight)
    else:
        weight_list[name] += int(weight)
    



def discount_offers(update,context):
    update.message.reply_text("""
        -> If you are buying items more than of Rs. 1000, than
        a discount of 5% will be given. 
        -> If you are buying items more than Rs. 2000, than
        a discount of 10% will be given
        -> If you are buying items more than Rs. 4000, than
        a discount of 20 % will be given
        -> If you are buying items more than Rs. 10000, than
        a discount of 25% will be given
        -> If you are buying items more than Rs. 20000, than
        a discount of 30% will be given
        -> If you are buying items more than Rs. 50000, than
        a discount of 50% will be given

        """
        
        )





def showInventory(update,context):
    
    items = list(Inventory_list.keys())
    Quantity = list(Inventory_list.values())
    update.message.reply_text("Your items list is->")
    update.message.reply_text(str(items))
    update.message.reply_text("your quantity list is ->")
    update.message.reply_text(str(Quantity))
    weight = list(weight_list.values())
    update.message.reply_text("Your weight list sum of all the products in kgs is->")
    wei =  sum(weight_list.values())/1000
    update.message.reply_text(str(wei))


def TotalPrice_with_discount(update,context):
    a = sum(price)
    update.message.reply_text("Total price without discount")
    update.message.reply_text(str(a))
    if a<=1000:
        update.message.reply_text("Total price after discount")
        update.message.reply_text(str(price))
        update.message.reply_text(str(a))
    elif a>1000 and a<2000:
        a = (95*a)/100
        update.message.reply_text("Total price after discount")
        update.message.reply_text(str(price))
        update.message.reply_text(str(a))
    elif a>2000 and a<4000:
        a = (90*a)/100
        update.message.reply_text("Total price after discount")
        update.message.reply_text(str(price))
        update.message.reply_text(str(a))
    elif a > 4000 and a < 10000:
        a = (80*a)/100
        update.message.reply_text("Total price after discount")
        update.message.reply_text(str(price))
        update.message.reply_text(str(a))
    elif a > 10000 and a < 20000:
        a = (75*a)/100
        update.message.reply_text("Total price after discount")
        update.message.reply_text(str(price))
        update.message.reply_text(str(a))
    elif a > 20000 and a < 50000:
        a = (70*a)/100
        update.message.reply_text("Total price after discount")
        update.message.reply_text(str(price))
        update.message.reply_text(str(a))
    else:
        a = (50*a)/100
        update.message.reply_text("Total price after discount")
        update.message.reply_text(str(price))
        update.message.reply_text(str(a))



def Cookies_family(update,context):
    name,quantity = context.args[0],context.args[1]

    if cookies_quantity[name] - int(quantity) > 0:
        cookies_quantity[name] -= int(quantity)
        p = cookies_price[name] * int(quantity)
        price.append(p)
    elif cookies_quantity[name] - int(quantity) == 0:
        cookies_quantity[name] -= int(quantity)
        p = cookies_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(cookies_quantity)
        update.message.reply_text("You can see the available quantity of cookies")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of cookies  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * cookies_weight_gms[name]
    Total_weight(name,int(weight),weight_list)



def HairCare_Products(update,context):

    
    name,quantity = context.args[0],int(context.args[1])

    if haircare_quantity[name] - int(quantity) > 0:
        haircare_quantity[name] -= int(quantity)
        p = haircare_price[name] * int(quantity)
        price.append(p)
    elif haircare_quantity[name] - int(quantity) == 0:
        haircare_quantity[name] -= quantity
        p = haircare_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(haircare_quantity)
        update.message.reply_text("You can see the available quantity of haircare")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of haircare  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * haircare_weight_ml[name]
    Total_weight(name,weight,weight_list)
      
        


def FastFood_Products(update,context):

   

    name,quantity = context.args[0],int(context.args[1])

    if fastfood_quantity[name] - int(quantity) > 0:
        fastfood_quantity[name] -= quantity
        p = fastfood_price[name] * int(quantity)
        price.append(p)
    elif fastfood_quantity[name] - int(quantity) == 0:
        fastfood_quantity[name] -= quantity
        p = fastfood_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(fastfood_quantity)
        update.message.reply_text("You can see the available quantity of fastfood")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of fastfood  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * fastfood_weight_gms[name]
    Total_weight(name,weight,weight_list)


def Dried_Vegis(update,context):

  


    name,quantity = context.args[0],int(context.args[1])

    if dried_vegis_quantity[name] - int(quantity) > 0:
        dried_vegis_quantity[name] -= quantity
        p = dried_vegis_price[name] * int(quantity)
        price.append(p)
    elif dried_vegis_quantity[name] - int(quantity) == 0:
        dried_vegis_quantity[name] -= quantity
        p = dried_vegis_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(dried_vegis_quantity)
        update.message.reply_text("You can see the available quantity of dried_vegis")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of dired_vegis  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)    
    weight = int(quantity) * dried_vegis_weight_gms[name]
    Total_weight(name,weight,weight_list)


def Dry_Fruits(update,context):

    
    
    name,quantity = context.args[0],int(context.args[1])

    if dry_fruits_quantity[name] - int(quantity) > 0:
        dry_fruits_quantity[name] -= quantity
        p = dry_fruits_price[name] * int(quantity)
        price.append(p)
    elif dry_fruits_quantity[name] - int(quantity) == 0:
        dry_fruits_quantity[name] -= quantity
        p = dry_fruits_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(dry_fruits_quantity)
        update.message.reply_text("You can see the available quantity of dry_fruits")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of dry_fruits  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * dry_fruits_weight_gms[name]
    Total_weight(name,weight,weight_list)
    

def Soap(update,context):


   
    name,quantity = context.args[0],int(context.args[1])

    if soap_quantity[name] - int(quantity) > 0:
        soap_quantity[name] -= quantity
        p = soap_price[name] * int(quantity)
        price.append(p)
    elif soap_quantity[name] - int(quantity) == 0:
        soap_quantity[name] -= quantity
        p = soap_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(soap_quantity)
        update.message.reply_text("You can see the available quantity of soap")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of soap  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * soap_weight_gms[name]
    Total_weight(name,weight,weight_list)


def Flour(update,context):



    name,quantity = context.args[0],int(context.args[1])

    if flour_quantity[name] - int(quantity) > 0:
        flour_quantity[name] -= quantity
        p = flour_price[name] * int(quantity)
        price.append(p)
    elif flour_quantity[name] - int(quantity) == 0:
        flour_quantity[name] -= quantity
        p = flour_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(flour_quantity)
        update.message.reply_text("You can see the available quantity of flour")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of flour  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * flour_weight_gms[name]
    Total_weight(name,weight,weight_list)

def Amul(update,context):

  

    name,quantity = context.args[0],int(context.args[1])

    if amul_quantity[name] - int(quantity) > 0:
        amul_quantity[name] -= quantity
        p = amul_price[name] * int(quantity)
        price.append(p)
    elif amul_quantity[name] - int(quantity) == 0:
        amul_quantity[name] -= quantity
        p = amul_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(amul_quantity)
        update.message.reply_text("You can see the available quantity of amul")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of amul  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * amul_weight_gms[name]
    Total_weight(name,weight,weight_list)

def DairyMilk_Chocolates(update,context):



        
    name,quantity = context.args[0],int(context.args[1])

    if dairymilk_quantity[name] - int(quantity) > 0:
        dairymilk_quantity[name] -= quantity
        p = dairymilk_price[name] * int(quantity)
        price.append(p)
    elif dairymilk_quantity[name] - int(quantity) == 0:
        dairymilk_quantity[name] -= quantity
        p = dairymilk_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(dairymilk_quantity)
        update.message.reply_text("You can see the available quantity of dairymilk")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of dairymilk  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * dairymilk_weight_gms[name]
    Total_weight(name,weight,weight_list)





def Stationary_products(update,context):

        
    name,quantity = context.args[0],int(context.args[1])

    if Stationary_products_quantity[name] - int(quantity) > 0:
        Stationary_products_quantity[name] -= quantity
        p = Stationary_products_price[name] * int(quantity)
        price.append(p)
    elif Stationary_products_quantity[name] - int(quantity) == 0:
        Stationary_products_quantity[name] -= quantity
        p = Stationary_products_price[name] * int(quantity)
        price.append(p)
    else:
        update.message.reply_text(
            """
            
            Sorry we don't have these many quantity to sell
            
            """)
        new = json.dumps(Stationary_products_quantity)
        update.message.reply_text("You can see the available quantity of Stationary")
        update.message.reply_text(new)
        update.message.reply_text("All the packets of Stationary  we have are of 500 gms")
    SeeInventory(name,int(quantity),Inventory_list)
    weight = int(quantity) * Stationary_products_weight_gms[name]
    Total_weight(name,weight,weight_list)





def delivery_options(update,context):
    got = context.args[0]
    got = got.lower()
    if got =="home":
        update.message.reply_text("""
            Your order Will be sent to home
        """)
    else:
        update.message.reply_text("""
        
        Your order is ready ,you can come to pick up

        """)


def add_order(update,context):

    update.message.reply_text("""
        You can add new order on the given link below by filling the details
    
    """
    
    )
    update.message.reply_text("Link is: https://docs.google.com/spreadsheets/d/10_5RWRoVqjQ2GS4OTzgHRi4zs8pPEpgJHWpnDXITOfA/edit?usp=sharing")



def book_order(update,context):
    got = context.args[0]
    got = got.lower()
    if got == 'yes':
        update.message.reply_text(
        """

            Thankyou  for shopping from our general store ,
            your order is done.
            You can see the items you purchased by using /showInventory
            For seeing the total price ,use -> /TotalPrice_with_discount
            Hope ,you liked coming here.

            The shopkeeper has received your order
        """)

    else:
        update.message.reply_text(
            """

            Sorry,but your orders couldn't be booked

        """
        )

dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('help',help))
dispatcher.add_handler(telegram.ext.CommandHandler('Cookies_family',Cookies_family))
dispatcher.add_handler(telegram.ext.CommandHandler('content',content))
dispatcher.add_handler(telegram.ext.CommandHandler('Cookies_names',Cookies_names))
dispatcher.add_handler(telegram.ext.CommandHandler('HairCare_Products',HairCare_Products))
dispatcher.add_handler(telegram.ext.CommandHandler("HairCare_Products_name",HairCare_Products_name))
dispatcher.add_handler(telegram.ext.CommandHandler("Soap",Soap))
dispatcher.add_handler(telegram.ext.CommandHandler("Soap_name",Soap_name))
dispatcher.add_handler(telegram.ext.CommandHandler("FastFood_Products",FastFood_Products))
dispatcher.add_handler(telegram.ext.CommandHandler("FastFood_name",FastFood_name))
dispatcher.add_handler(telegram.ext.CommandHandler("Dried_Vegis",Dried_Vegis))
dispatcher.add_handler(telegram.ext.CommandHandler("Dried_Vegis_name",Dried_Vegis_name))
dispatcher.add_handler(telegram.ext.CommandHandler("Dry_Fruits",Dry_Fruits))
dispatcher.add_handler(telegram.ext.CommandHandler("Dry_Fruits_name",Dry_Fruits_name))
dispatcher.add_handler(telegram.ext.CommandHandler("Flour",Flour))
dispatcher.add_handler(telegram.ext.CommandHandler("Flour_name",Flour_name))
dispatcher.add_handler(telegram.ext.CommandHandler("Amul",Amul))
dispatcher.add_handler(telegram.ext.CommandHandler("Amul_product_name",Amul_product_name))
dispatcher.add_handler(telegram.ext.CommandHandler("DairyMilk_Chocolates",DairyMilk_Chocolates))
dispatcher.add_handler(telegram.ext.CommandHandler("DairyMilk_product_name",DairyMilk_product_name))
dispatcher.add_handler(telegram.ext.CommandHandler("Stationary_products",Stationary_products))
dispatcher.add_handler(telegram.ext.CommandHandler("Stationary_products_name",Stationary_products_name))
dispatcher.add_handler(telegram.ext.CommandHandler("TotalPrice_with_discount",TotalPrice_with_discount))
dispatcher.add_handler(telegram.ext.CommandHandler("showInventory",showInventory))
dispatcher.add_handler(telegram.ext.CommandHandler("book_order",book_order))
dispatcher.add_handler(telegram.ext.CommandHandler("add_order",add_order))
dispatcher.add_handler(telegram.ext.CommandHandler("Inventory",Inventory))
dispatcher.add_handler(telegram.ext.CommandHandler("delivery_options",delivery_options))
dispatcher.add_handler(telegram.ext.CommandHandler("discount_offers",discount_offers))





updater.start_polling()
updater.idle()



