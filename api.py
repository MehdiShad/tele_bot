import requests

def invitation_templates():
    # ca_cert_path = '/path/to/your/certificate.bundle'
    # ca_cert_path = 'd:\mehdi\learning\python\telegram - python\telegrambot-philolearn\.venv\lib\site-packages'
    # api = requests.get('https://u.davat.app/Api/V1/Invitation/InvitationTemplateInfoApi/', verify=ca_cert_path)
    # res_api = api.jsona()
    response = {
        "all_templates": 135,
        "active_templates": 54,
        "draft_templates": 1
    }
    return response

invitation_templates()