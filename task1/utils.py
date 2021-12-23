def get_data(request):
    data = request.headers.get("data")
    entities = data.split('%%')
    entities_data = {}
    for entity in entities:
        name, *args = entity.split('&&')
        keys = [key for key in args[::2] if key]
        values = [value for value in args[1::2] if value]
        data_dct = dict(zip(keys, values))
        entities_data.update({name: data_dct})
    return entities_data


def get_request_id(request):
    return request.headers.get("request_id")
