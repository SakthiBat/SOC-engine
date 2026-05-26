import os
from modules.monitor import follow
from modules.detector import detect_suspicious
from modules.mailer import send_email
from modules.logger import save_alert


def main():

    os.system("clear")
    os.system('figlet "SIGMA ENGINE"')
    os.system('toilet -f term -F border "REAL-TIME SOC MONITOR"')

    loglines = follow()

    for line in loglines:

        alerts = detect_suspicious(line)

        if alerts:

            for alert in alerts:

                print(f"[ALERT] {alert}")

                print(line)

                save_alert(alert, line)

                send_email(
                    subject=f"SOC ALERT: {alert}",
                    body=f"""
Alert Type: {alert}

Detected Log:
{line}
"""
                )


if __name__ == "__main__":
    main()
