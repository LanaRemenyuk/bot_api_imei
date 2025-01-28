import requests

class IMEIService:
    """Сервис для работы с API IMEI"""

    @staticmethod
    def check_imei_is_valid(imei, token, service_id=12):
        url = 'https://api.imeicheck.net/v1/checks'
        headers = {
            'Authorization': f'Bearer {token}',
            'Accept-Language': 'en'
        }
        payload = {
            'deviceId': imei,
            'serviceId': service_id
        }

        try:
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 201:
                data = response.json()
                return data.get("properties", {})

            if response.status_code == 422:
                error_details = response.json().get("errors", {})
                device_id_errors = error_details.get("deviceId", [])
                if device_id_errors:
                    error_message = device_id_errors[0]
                    if "device id" in error_message.lower():
                        error_message = "IMEI должен быть длиной от 8 до 15 символов."
                    elif "selected deviceId is invalid" in error_message.lower():
                        error_message = "Выбранный IMEI недействителен. Пожалуйста, проверьте правильность IMEI."
                    return {'error': f"Пожалуйста, проверьте корректность формата IMEI и введите его заново."}

            error_messages = {
                400: "Неверный запрос. Пожалуйста, проверьте параметры.",
                401: "Неавторизованный доступ. Проверьте ваш токен.",
                403: "Доступ запрещен. Убедитесь, что у вас есть права для выполнения этого действия.",
                404: "Не найдено. Возможно, устройство с таким IMEI не зарегистрировано.",
                500: "Ошибка на сервере. Попробуйте позже.",
                502: "Ошибка шлюза. Сервер не доступен.",
                503: "Сервис временно недоступен. Попробуйте снова позже.",
            }

            error_message = error_messages.get(response.status_code, "Неизвестная ошибка.")
            return {'error': f'{error_message} Код ошибки: {response.status_code}'}

        except requests.exceptions.Timeout:
            return {'error': "Ошибка подключения: запрос превысил время ожидания. Попробуйте позже."}
        except requests.exceptions.TooManyRedirects:
            return {'error': "Ошибка подключения: слишком много перенаправлений. Проверьте URL."}
        except requests.exceptions.RequestException as e:
            return {'error': f"Ошибка запроса: {str(e)}. Проверьте ваше интернет-соединение."}

