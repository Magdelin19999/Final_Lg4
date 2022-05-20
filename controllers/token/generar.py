from itsdangerous import URLSafeTimedSerializer, SignatureExpired

from models.mensaje.mensaje import mensaje

s = URLSafeTimedSerializer("Thisisasecret")

# correo='jeisonmavisoyface@gmail.com'
# token=s.dumps(correo, salt='id-confirm')
def generarKey(id):
    return s.dumps(id, salt="id-confirm")


def returnID(token):
    resultado = False
    id=0
    try:
        id = s.loads(token, salt="id-confirm", max_age=60)
        
        print("returnID")
        resultado = True

    except SignatureExpired:
        
        resultado = resultado
    print('\n\n\n\n\n\n\n\n',id)

    return {"resultado":resultado,"id":id}
