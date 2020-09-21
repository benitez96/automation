#%% EJEMPLOS PARA UTILIZAR LIBRERIA
import bs4                  #(bs4)--> pip install beautifulsoup4
import requests
# obtenemos el cod HTML de la pagina
res = requests.get('https://articulo.mercadolibre.com.ar/MLA-763083163-banda-de-lija-tela-de-75x457-g-60-80-100-y-120-x-10u-doblea-_JM#reco_item_pos=2&reco_backend=second_best_buying_trend&reco_backend_type=function&reco_client=home_second-best-buying-trend-recommendations&reco_id=09d010bb-9ce1-48fb-9e20-a1e703ccae12&c_id=/home/second-best-trends-recommendations/element&c_element_order=3&c_uid=86390e63-2bcd-4d6b-b651-aff0be221222')
#checkeamos que todo este ok
res.raise_for_status()
#creamos un objeto beatifulsoup -> recibe 2 parametros
soup = bs4.BeautifulSoup(res.text, features="html.parser")
#seleccionas la RUTA CSS a analizar y lo almacenamos en una variable
elem  = soup.select('html body main#root-app div.ui-vip-core div.ui-pdp-container.ui-pdp-container--pdp div.ui-pdp-container__row.ui-pdp--relative.pb-40 div.ui-pdp-container__col.col-1.ui-pdp-container--column-right.mt-16.pr-16 div.ui-pdp-container__row.ui-pdp-component-list.pr-16.pl-16 div.ui-pdp-container__col.col-2.ui-vip-core-container--short-description.ui-vip-core-container--column__right div.ui-pdp-container__row.ui-pdp-container__row--price div.ui-pdp-price.mt-16.ui-pdp-price--size-large div.andes-tooltip__trigger div.ui-pdp-price__second-line span.price-tag.ui-pdp-price__part span.price-tag-fraction')
#elem es una lista de 1(un) solo elemento.
print(elem[0])
#si queremos el en formato texto
print(elem[0].text)
#si queremos un texto limpio
print(elem[0].text.strip())

#%% PROGRAMA UTIL
import bs4, requests

def getMercadoLibrePrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body main#root-app div.ui-vip-core div.ui-pdp-container.ui-pdp-container--pdp div.ui-pdp-container__row.ui-pdp--relative.pb-40 div.ui-pdp-container__col.col-1.ui-pdp-container--column-right.mt-16.pr-16 div.ui-pdp-container__row.ui-pdp-component-list.pr-16.pl-16 div.ui-pdp-container__col.col-2.ui-vip-core-container--short-description.ui-vip-core-container--column__right div.ui-pdp-container__row.ui-pdp-container__row--price div.ui-pdp-price.mt-16.ui-pdp-price--size-large div.andes-tooltip__trigger div.ui-pdp-price__second-line span.price-tag.ui-pdp-price__part span.price-tag-fraction')
    price = elems[0].text.strip()
    return price

precio = getMercadoLibrePrice('https://articulo.mercadolibre.com.ar/MLA-673506984-anteojos-lentes-de-sol-vulk-the-guardian-wayfarer-gafas-_JM?searchVariation=57357068943#searchVariation=57357068943&position=5&type=item&tracking_id=2dd13e27-84df-4054-a9ad-4771d7869889')
print('el precio es: ', precio)

# %%
