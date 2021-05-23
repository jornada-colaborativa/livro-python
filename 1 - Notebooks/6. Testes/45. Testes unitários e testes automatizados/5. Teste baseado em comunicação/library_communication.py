class LibraryCommunication:
    def __init__(self, communication_service):
        self.communication_service = communication_service

    def send_return_warning(self, email_address):
        # modulo a ser testado
        text = "Your loan period ends tomorrow. Please " \
               "remember to return or renew your books"
        self.communication_service.send_email(email_address, text)
