class ArbolHuffman:
    @staticmethod
    def decodificar_mensaje(mensaje_codificado, arbol_huffman):
        nodo_actual = arbol_huffman
        mensaje_decodificado = ""

        for bit in mensaje_codificado:
            if bit == "0":
                nodo_actual = nodo_actual.left
            else:
                nodo_actual = nodo_actual.right

            if nodo_actual.char is not None:
                mensaje_decodificado += nodo_actual.char
                nodo_actual = arbol_huffman

        return mensaje_decodificado



mensaje_codificado1 = (
    "100010111010110000101110100011100000110110000001111001111010010110"
    "0001101001110011010001011101011111110100001111001111110011110100011000110000"
    "00101101011110111111101110101101101110011101101111001111111001010010100101000001"
    "011010110001011001101000111001001011000011001000110101101010111111111110110111"
    "0111001000010010101100011111110001000111011001100101101000110111110101101000"
    "1101110000000111001001010100011111100001100101101011100110011110100011000110"
    "000001011010111110011100"
)

mensaje_codificado2 = (
    "01101010110111001010001111010111001101110101101101000010001110101001"
    "011110100111111101110010100011110101110011011101011000011000100110100011100100"
    "10001100010110011001110010010000111101111010"
)

mensaje_decodificado1 = ArbolHuffman.decodificar_mensaje(mensaje_codificado1, )
mensaje_decodificado2 = ArbolHuffman.decodificar_mensaje(mensaje_codificado2,)

print("Mensaje 1 decodificado:")
print(mensaje_decodificado1)
print("\nMensaje 2 decodificado:")
print(mensaje_decodificado2)
