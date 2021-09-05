class Urls:
    MAIN_LINK = 'https://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = MAIN_LINK + 'accounts/login/'
    PRODUCT_BASE_LINK = MAIN_LINK + 'catalogue/'
    PRODUCT_95 = 'the-city-and-the-stars_95'
    PRODUCT_207 = 'coders-at-work_207'
    PRODUCT_209 = 'the-shellcoders-handbook_209'

    @staticmethod
    def get_product_link(product: str, promo: str = None):
        attributes = ('?' if promo else '') + f'promo={promo}' if promo else ''
        return f'{Urls.PRODUCT_BASE_LINK}{product}/{attributes}'
