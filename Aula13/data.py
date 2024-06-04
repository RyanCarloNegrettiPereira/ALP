from datetime import datetime
def valida_data(data):
    try:
        data_obj = datetime.strptime(data, "%d/%m/%Y")
        hoje=datetime.now().date()
        idade=hoje.year-data_obj.year-((hoje.month, hoje.day)<(data_obj.month, data_obj.day))
        if idade<18:
            return False
        return True
    except ValueError:
        return False