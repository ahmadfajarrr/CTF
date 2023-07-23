from PIL import Image

def color_inversion(image_path, output_path):
    # Buka gambar menggunakan PIL
    img = Image.open(image_path)

    # Dapatkan ukuran gambar
    width, height = img.size

    # Loop melalui setiap piksel dan lakukan operasi XOR dengan nilai 255 (maksimum nilai piksel)
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            inverted_pixel = tuple(255 - value for value in pixel)
            img.putpixel((x, y), inverted_pixel)

    # Simpan gambar hasil inversi
    img.save(output_path)

if __name__ == "__main__":
    input_image_path = "fish.png"  # Ganti dengan path gambar input Anda
    output_image_path = "output_image.png"  # Ganti dengan path tempat menyimpan gambar hasil inversi
    color_inversion(input_image_path, output_image_path)
