from apps.core.models import Branch


def get_branch(user, branch_id):
    branch = Branch.objects.get(pk=branch_id)
    if branch.company.owner != user:
        return False
    else:
        return branch
