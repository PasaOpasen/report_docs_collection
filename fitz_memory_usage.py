
import gc
import psutil
import fitz

def get_memory_usage():
    gc.collect()
    return psutil.Process().memory_info().rss / 1024 ** 2

def func(pdf_path: str):

    with fitz.open(pdf_path) as doc:

        for page in doc:
            images = page.get_images(True)
            if not images:
                continue
            xref = images[0][0]

            page.get_image_rects(xref)  # doesn't free memory
            


doc = './TFCV.pdf'  # 482 pages


print('on start:')
print(get_memory_usage())
print()

for _ in range(25):

    func(doc)
    print(get_memory_usage())

print()
print('before exit:')
print(get_memory_usage())


