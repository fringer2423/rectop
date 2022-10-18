import qrcode

from PIL import Image

from django.core.files.storage import FileSystemStorage
from django.conf import settings

from apps.core.models import QRCode

from .branch_service import verification_owner_branch


def generate_qc_code(slug):
    qr_url = f'https://www.rectop.ru/qrcoderates/{slug}'

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(qr_url)
    qr.make()
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    logo = Image.open(str(settings.BASE_DIR) + "/static/images/qr_code_favicon.jpg")
    pos = ((qr_image.size[0] - logo.size[0]) // 2, (qr_image.size[1] - logo.size[1]) // 2)
    qr_image.paste(logo, pos)

    fs = FileSystemStorage(
        location=str(settings.BASE_DIR) + "/media/branch/qrcode",
        base_url="branch/qrcode",
    )

    qr_name_image = fs.get_available_name("QRcode.png")
    qr_image_url = f'{settings.BASE_DIR}/media/branch/qrcode/{qr_name_image}'

    qr_image.save(qr_image_url, format="png")
    return qr_name_image


def create_qrcode_by_branch_id(user, branch_id):
    if verification_owner_branch(user, branch_id):
        new_qrcode = QRCode.objects.create(branch_id=branch_id)

        qr_name_image = generate_qc_code(new_qrcode.slug_name)

        new_qrcode.image = f'/media/branch/qrcode/{qr_name_image}'

        new_qrcode.save()

        return new_qrcode
    else:
        return False


def get_qrcode_by_id(user, qrcode_id):
    qr_code = QRCode.objects.get(pk=qrcode_id)
    if verification_owner_branch(user=user, branch_id=qr_code.branch_id):
        return qr_code
    else:
        return False


def get_all_qrcode():
    qrcodes_list = QRCode.objects.all()
    return qrcodes_list
