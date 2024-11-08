import pyautogui
import uuid


def verify_fishing():
    max_attempts = 100
    for attempt in range(1, max_attempts + 1):
        try:
            pyautogui.locateOnScreen("./assets/rod.png", confidence=0.8)

            print(f"Pescou! Tentativa {attempt}/{max_attempts}")
            reel()
            break

        except:
            print(f"Verificando pesca... Tentativa {attempt}/{max_attempts}")
            pyautogui.sleep(1)


def cast_rod():
    print("Iniciando pesca...")
    pyautogui.mouseDown(x=960, y=540)
    pyautogui.sleep(3)
    pyautogui.mouseUp()

    verify_fishing()


def reel():
    print("Pescando peixe...")
    pyautogui.mouseDown(x=960, y=540)

    max_attempts = 100
    for attempt in range(1, max_attempts + 1):
        try:
            pyautogui.locateOnScreen("./assets/catch.png", confidence=0.8)
            pyautogui.sleep(1)

            pyautogui.screenshot(f"./screenshots/fish_{uuid.uuid4().hex}.png")
            print(f"Pesca finalizada! Tentativa {attempt}/{max_attempts}")

            pyautogui.keyDown("e")
            pyautogui.keyUp("e")

            pyautogui.sleep(1)
            cast_rod()
            break

        except:
            print(f"Aguardando finalização... Tentativa {attempt}/{max_attempts}")
            pyautogui.sleep(1)


cast_rod()
