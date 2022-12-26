from typing import Optional, Tuple
import smtplib
from dataclasses import dataclass


@dataclass
class GmailServer:
    """The Gmail server cna be used as a context manager of hte email service
    provided by google

    Example
    ---
    ```python
    with GmailServer(email_username,email_password) as email:
      email.send_email("hello how are you", "kisoko1@sheffield.ac.uk")
    ```
    """
    # Set the email server and credentials
    email_password: str
    email_username: str
    __server = smtplib.SMTP('smtp.gmail.com', 587)

    def set_server(self, server: smtplib.SMTP):
        self.__server = server

    @property
    def server(self) -> smtplib.SMTP:
        return self.__server

    def __enter__(self):
        # set the login and credentials
        self.server.starttls()
        self.server.login(self.email_username, self.email_password)
        return self

    def __exit__(self) -> None:
        # Close the server connection
        self.server.quit()

    def __build_mail(self, to: str, subject: Optional[str]) -> Tuple[str]:
        # Set the email headers
        headers = f'Subject: {"" if subject is None else subject}\n'
        headers += f"To: {to}\n"
        headers += "Content-Type: text/html; charset=utf-8\n"
        return to, headers

    def send_email(self, body: str, to: str, subject: Optional[str] = None) -> None:
        # Send the email
        to, headers = self.__build_mail(to, subject=subject)
        self.server.sendmail(self.email_username, to, headers + body)
