******************
Mercado Libre MELI
******************

:Date: |today|

Client of the Mercado Libre's API

get
===

    Issues a get request to the path and passes the kwargs as get parameters.


post
====

    Issues a post request to the path and passes the data as the request body
    and the kwargs as get parameters.

    data could be a json string or a dictionary.

    This usually needs the access_token, so, pass the access=True as a argument
    this will put the access_token within the get parameters.

    obs: you need to set the access_token first.


help
====

    Get the help from the API.

    ex: meli.help('items')

    would generate a large text with examples, arguments, methods etc...


