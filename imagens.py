from PIL import Image, ImageFilter, ImageOps
import os

def abrir_imagem(caminho):
    try:
        imagem = Image.open(caminho)
        print(f"Imagem {caminho} aberta com sucesso.")
        return imagem
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None

def aplicar_filtro(imagem):
    try:
        imagem_filtro = imagem.filter(ImageFilter.CONTOUR)  # Aplicar filtro de contorno
        print("Filtro aplicado com sucesso.")
        return imagem_filtro
    except Exception as e:
        print(f"Erro ao aplicar filtro: {e}")
        return None

def redimensionar_imagem(imagem, tamanho):
    try:
        imagem_redimensionada = imagem.resize(tamanho)  # Redimensionar para o tamanho fornecido
        print(f"Imagem redimensionada para {tamanho}.")
        return imagem_redimensionada
    except Exception as e:
        print(f"Erro ao redimensionar imagem: {e}")
        return None

def salvar_imagem(imagem, caminho_saida):
    try:
        imagem.save(caminho_saida)
        print(f"Imagem salva em {caminho_saida}.")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")

def converter_para_preto_e_branco(imagem):
    try:
        imagem_p_b = ImageOps.grayscale(imagem)  # Converter para preto e branco
        print("Imagem convertida para preto e branco.")
        return imagem_p_b
    except Exception as e:
        print(f"Erro ao converter para preto e branco: {e}")
        return None

def main():
    # Caminho para a imagem de entrada
    caminho_imagem = 'exemplo.jpg'  # Substitua pelo caminho da sua imagem

    # Verifique se o arquivo existe
    if not os.path.isfile(caminho_imagem):
        print(f"O arquivo {caminho_imagem} não foi encontrado.")
        return

    # Abrir imagem
    imagem = abrir_imagem(caminho_imagem)

    if imagem:
        # Aplicar filtro
        imagem_filtro = aplicar_filtro(imagem)

        if imagem_filtro:
            # Redimensionar imagem
            imagem_redimensionada = redimensionar_imagem(imagem_filtro, (800, 600))

            if imagem_redimensionada:
                # Converter para preto e branco
                imagem_p_b = converter_para_preto_e_branco(imagem_redimensionada)

                if imagem_p_b:
                    # Salvar imagem final
                    salvar_imagem(imagem_p_b, 'imagem_processada.jpg')

if __name__ == "__main__":
    main()
