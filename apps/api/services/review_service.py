from apps.core.models import Review

from .branch_service import get_branch_by_branch_id, verification_owner_branch


def get_review_by_id(user, review_id):
    review = Review.objects.get(pk=review_id)
    if verification_owner_branch(user=user, branch_id=review.branch_id):
        return review
    else:
        return False


def create_review_by_branch_id(user, branch_id, full_name, link, rating):
    if verification_owner_branch(user=user, branch_id=branch_id):
        review = Review.objects.create(branch_id=branch_id, full_name=full_name, link=link, rating=rating)
        return review
    else:
        return False
