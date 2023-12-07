import configuration
import requests
import data

post_creat_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                                 json=data.create_order_body,
                                 headers=data.headers)

order_body = post_creat_order.json()
current_track_number = order_body["track"]

get_order_by_number = requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER_BY_NUMBER_PATH
                                   + str(current_track_number))