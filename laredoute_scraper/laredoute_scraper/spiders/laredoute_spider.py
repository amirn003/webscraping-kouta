import scrapy

class LaredouteSpider(scrapy.Spider):
    name = 'laredoute_spider'
    allowed_domains = ['laredoute.fr']
    start_urls = ['https://www.laredoute.fr/ppdp/prod-554346844.aspx']

    def parse(self, response):
        yield {
            "Catalogue": response.css('span.catalog::text').get(),
            "Nom commercial": response.css('h1.product-name::text').get(),
            "Marque": response.css('span.brand-name::text').get(),
            "Type de produit": response.css('span.product-type::text').get(),
            "Pièce": response.css('span.room::text').get(),
            "Catégorie": response.css('span.category::text').get(),
            "Sous-catégorie": response.css('span.subcategory::text').get(),
            "Couleurs": response.css('span.colors::text').get(),
            "Matières": response.css('span.materials::text').get(),
            "Profondeur": response.css('span.depth::text').get(),
            "Longueur": response.css('span.length::text').get(),
            "Hauteur": response.css('span.height::text').get(),
            "Prix": response.css('span.price::text').get(),
            "Référence": response.css('span.reference::text').get(),
            "URL": response.url,
            "Lien Web": response.url,
            "Photos Produits": response.css('img.product-image::attr(src)').getall()
        }
