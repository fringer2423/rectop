import qrcode

from PIL import Image

from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models import QuerySet

from apps.core.models import QRCode, User

from .branch_service import verification_owner_branch_service


def generate_qc_code_service(slug: str) -> object:
    """
    Функция генерирует QRCode и сохраняет его
    :param slug: ссылка
    :return: qr_image_name
    """
    qr_url: str = f'https://www.rectop.ru/qrcoderates/{slug}'

    qr: object = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(qr_url)
    qr.make()
    qr_image: object = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    logo: object = Image.open(str(settings.BASE_DIR) + "/static/images/qr_code_favicon.jpg")
    pos: object = ((qr_image.size[0] - logo.size[0]) // 2, (qr_image.size[1] - logo.size[1]) // 2)
    qr_image.paste(logo, pos)

    fs: object = FileSystemStorage(
        location=str(settings.BASE_DIR) + "/media/branch/qrcode",
        base_url="branch/qrcode",
    )

    qr_name_image: object = fs.get_available_name("QRcode.png")
    qr_image_url: object = f'{settings.BASE_DIR}/media/branch/qrcode/{qr_name_image}'

    qr_image.save(qr_image_url, format="png")

    return qr_name_image


def create_qrcode_by_branch_id_service(user: QuerySet[User], branch_id: int) -> QuerySet[QRCode] | None:
    """
    Функция создает QRCode по branch id и возвращает его, если есть доступ. Иначе вернет None
    :param user: Текущий пользователь
    :param branch_id: id филиала
    :return: optional: QRCode
    """
    result: QuerySet[QRCode] | None = (
        None,
        _create_qrcode_by_branch_id_service(branch_id=branch_id)
    )[verification_owner_branch_service(user, branch_id)]

    return result


def _create_qrcode_by_branch_id_service(branch_id: int) -> QuerySet[QRCode]:
    """
    Функция создает QRCode по branch id
    :param branch_id: branch id
    :return: branch
    """
    new_qrcode: QuerySet[QRCode] = QRCode.objects.create(branch_id=branch_id)

    qr_name_image: object = generate_qc_code_service(new_qrcode.slug_name)

    new_qrcode.image = f'/media/branch/qrcode/{qr_name_image}'

    new_qrcode.save()

    return new_qrcode


def get_qrcode_by_id_service(user: QuerySet[User], qrcode_id: int) -> QuerySet[QRCode] | None:
    """
    Функция возвращает QRCode по id, если есть доступ, иначе вернется None
    :param user: Текущий пользователь
    :param qrcode_id: id QRCode
    :return: optional: QRCode
    """
    qr_code: QuerySet[QRCode] = QRCode.objects.get(pk=qrcode_id)

    result: QuerySet[QRCode] | None = (
        None,
        qr_code
    )[
        verification_owner_branch_service(
            user=user,
            branch_id=qr_code.branch_id
        )
    ]

    return result


def get_all_qrcode_service() -> QuerySet[QRCode]:
    """
    Функция возвращает все QRCode
    :return: Все QRCode
    """
    qrcodes_list: QuerySet[QRCode] = QRCode.objects.all()
    return qrcodes_list
