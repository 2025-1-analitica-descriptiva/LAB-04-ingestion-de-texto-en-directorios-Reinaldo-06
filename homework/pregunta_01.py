# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import os 
import zipfile
import pandas as pd


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    input_zip_path = "./files/input.zip"
    extract_path = "./files/input"  # <- Aquí sí debe extraerse dentro de files/input

    # Descomprimir si no existe la carpeta
    if not os.path.exists(extract_path):
        with zipfile.ZipFile(input_zip_path, 'r') as zip_ref:
            zip_ref.extractall("./files")  # ZIP contiene la carpeta "input/"
    else:
        print("⚠️ La carpeta 'input' ya existe. No se descomprime nuevamente.")

    train_path = os.path.join(extract_path, 'train')
    test_path = os.path.join(extract_path, 'test')

    # Generar dataset de entrenamiento
    train_dataset = []
    for target in ["negative", "positive", "neutral"]:
        kind_path = os.path.join(train_path, target)
        for filename in os.listdir(kind_path):
            if filename.endswith('.txt'):
                with open(os.path.join(kind_path, filename), 'r', encoding='utf-8') as f:
                    phrase = f.read().strip()
                    train_dataset.append({
                        'phrase': phrase,
                        'target': target
                    })

    # Generar dataset de prueba
    test_dataset = []
    for target in ["negative", "positive", "neutral"]:
        kind_path = os.path.join(test_path, target)
        for filename in os.listdir(kind_path):
            if filename.endswith('.txt'):
                with open(os.path.join(kind_path, filename), 'r', encoding='utf-8') as f:
                    phrase = f.read().strip()
                    test_dataset.append({
                        'phrase': phrase,
                        'target': target
                    })

    # Convertir a DataFrame
    train_df = pd.DataFrame(train_dataset)
    test_df = pd.DataFrame(test_dataset)

    # Guardar los CSVs en la ruta esperada por el test
    output_dir = './files/output'
    os.makedirs(output_dir, exist_ok=True)

    train_df.to_csv(os.path.join(output_dir, 'train_dataset.csv'), index=False)
    test_df.to_csv(os.path.join(output_dir, 'test_dataset.csv'), index=False)

    return train_df, test_df


pregunta_01()

