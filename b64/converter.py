import base64

def transforma_img_str(imagem):
    with open(imagem, "rb") as arquivo_imagem:
        bytes_base64 = base64.b64encode(arquivo_imagem.read())

        string_base64 = bytes_base64.decode("utf-8")
        return string_base64
    
imagem_string = transforma_img_str("assets/feijao.png")
print(imagem_string)