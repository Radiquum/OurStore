# NashStore API

"reverse enginiring" of NashStore.ru API

## Required headers

```h
    "content-type": "application/json",
    "user-agent": "Nashstore"
```

## Actual app version

METHOD: GET

URL: "https://store.nashstore.ru/api/v1/nashstore/version"

Responce:

``` json

    {
    "status": "success", 
    "version_code": 6, 
    "version_name": "0.0.6"
    }

```

## App Categories

### Avalible categories

METHOD: GET

URL: "https://store.nashstore.ru/api/mobile/v1/selections/applications"

2ndURL: "https://store.nashstore.ru/api/mobile/v1/categories/application"

<details> 
<summary>Responce:</summary>

```json

{
  "categories": [
    {
      "id": 2,
      "title": "Автомобили и транспорт",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 54
    },
    {
      "id": 3,
      "title": "Банки",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 20
    },
    {
      "id": 4,
      "title": "Бизнес",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app4.png",
      "count": 50
    },
    {
      "id": 5,
      "title": "Видеоплееры и редакторы",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 4
    },
    {
      "id": 6,
      "title": "Дополненная реальность",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app6.png",
      "count": 2
    },
    {
      "id": 7,
      "title": "Еда и напитки",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app7.png",
      "count": 18
    },
    {
      "id": 8,
      "title": "Жилье и дом",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 20
    },
    {
      "id": 9,
      "title": "Здоровье и фитнес",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app9.png",
      "count": 23
    },
    {
      "id": 10,
      "title": "Знакомства",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 14
    },
    {
      "id": 11,
      "title": "Инструменты",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app11.png",
      "count": 60
    },
    {
      "id": 12,
      "title": "Искусство и дизайн",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app12.png",
      "count": 2
    },
    {
      "id": 13,
      "title": "Карты и навигация",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app13.png",
      "count": 11
    },
    {
      "id": 14,
      "title": "Книги и справочники",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app14.png",
      "count": 45
    },
    {
      "id": 15,
      "title": "Комиксы",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app15.png",
      "count": 1
    },
    {
      "id": 16,
      "title": "Красота",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 5
    },
    {
      "id": 17,
      "title": "Материнство и детство",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app17.png",
      "count": 6
    },
    {
      "id": 18,
      "title": "Медицина",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app18.png",
      "count": 14
    },
    {
      "id": 19,
      "title": "Мероприятия",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 5
    },
    {
      "id": 20,
      "title": "Музыка и аудио",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app20.png",
      "count": 17
    },
    {
      "id": 21,
      "title": "Новости и журналы",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 16
    },
    {
      "id": 22,
      "title": "Образование",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app22.png",
      "count": 55
    },
    {
      "id": 23,
      "title": "Персонализация",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 15
    },
    {
      "id": 24,
      "title": "Погода",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app24.png",
      "count": 3
    },
    {
      "id": 25,
      "title": "Покупки",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app25.png",
      "count": 24
    },
    {
      "id": 26,
      "title": "Путешествия",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app26.png",
      "count": 22
    },
    {
      "id": 27,
      "title": "Работа",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app27.png",
      "count": 24
    },
    {
      "id": 28,
      "title": "Развлечения",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app28.png",
      "count": 51
    },
    {
      "id": 29,
      "title": "Связь",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app29.png",
      "count": 14
    },
    {
      "id": 30,
      "title": "Социальные",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app30.png",
      "count": 37
    },
    {
      "id": 31,
      "title": "Спорт",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app31.png",
      "count": 14
    },
    {
      "id": 32,
      "title": "Стиль жизни",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app32.png",
      "count": 11
    },
    {
      "id": 33,
      "title": "Финансы",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app33.png",
      "count": 34
    },
    {
      "id": 34,
      "title": "Фотография",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app34.png",
      "count": 4
    },
    {
      "id": 35,
      "title": "Другие",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 8
    },
    {
      "id": 1,
      "title": "Аниме",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game1.png",
      "count": 3
    },
    {
      "id": 2,
      "title": "Аркады",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game2.png",
      "count": 37
    },
    {
      "id": 3,
      "title": "Викторины",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game3.png",
      "count": 10
    },
    {
      "id": 4,
      "title": "Военные",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game4.png",
      "count": 2
    },
    {
      "id": 5,
      "title": "Головоломки",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game5.png",
      "count": 42
    },
    {
      "id": 6,
      "title": "Гонки",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game6.png",
      "count": 5
    },
    {
      "id": 7,
      "title": "Детские",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game7.png",
      "count": 11
    },
    {
      "id": 9,
      "title": "Инди",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game9.png",
      "count": 8
    },
    {
      "id": 11,
      "title": "Казуальные",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game11.png",
      "count": 22
    },
    {
      "id": 12,
      "title": "Карточные",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game12.png",
      "count": 11
    },
    {
      "id": 13,
      "title": "Квесты",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game13.png",
      "count": 1
    },
    {
      "id": 14,
      "title": "Логические",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game14.png",
      "count": 7
    },
    {
      "id": 15,
      "title": "Музыка",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game15.png",
      "count": 1
    },
    {
      "id": 16,
      "title": "Настольные игры",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game16.png",
      "count": 15
    },
    {
      "id": 17,
      "title": "Обучающие",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game17.png",
      "count": 5
    },
    {
      "id": 19,
      "title": "Приключения",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game19.png",
      "count": 17
    },
    {
      "id": 20,
      "title": "Ролевые",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game20.png",
      "count": 6
    },
    {
      "id": 21,
      "title": "Российские",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game21.png",
      "count": 4
    },
    {
      "id": 22,
      "title": "Симуляторы",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game22.png",
      "count": 23
    },
    {
      "id": 23,
      "title": "Словесные игры",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game23.png",
      "count": 16
    },
    {
      "id": 24,
      "title": "Спортивные игры",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game24.png",
      "count": 2
    },
    {
      "id": 25,
      "title": "Стратегии",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game25.png",
      "count": 6
    },
    {
      "id": 27,
      "title": "Фэнтези",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game27.png",
      "count": 1
    },
    {
      "id": 28,
      "title": "Шутеры",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game28.png",
      "count": 11
    },
    {
      "id": 29,
      "title": "Экшены",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game29.png",
      "count": 7
    },
    {
      "id": 30,
      "title": "MMORPG",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game30.png",
      "count": 2
    },
    {
      "id": 31,
      "title": "MOBA",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game31.png",
      "count": 1
    },
    {
      "id": 100,
      "title": "Другие",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game100.png",
      "count": 5
    }
  ],
  "limit": 10,
  "list": {},
  "page": 0,
  "positions": [],
  "status": "success",
  "total": 0
}

```

</details>

### Goto category

METHOD: GET

URL: "https://store.nashstore.ru/api/mobile/v1/categories/application/categoryID?page="

<details>
<summary>Responce: </summary>

```json

{
  "list": [
    {
      "id": "62801c234891a527a6f00cfe",
      "app_id": "com.aimp.player",
      "title": "AIMP",
      "short_description": "Это аудиоплеер на основе плейлистов для платформы Android",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/e4954fb66d98e2a01e9662c9",
      "rating": "4,93",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 11583352,
      "r_count": "",
      "ar": "6+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "23.2тыс.",
      "did": "62801b6c4891a527a6f00cec",
      "dtitle": "Artem Izmaylov",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 1193,
        "version_name": "v3.22, build 1193 (26.04.2022)",
        "create_at": "2022-05-14T21:29:31.777Z",
        "release_notes": "Первый публичный релиз на платформе",
        "install_path": "https://cdnb.nashstore.ru/store/install/62801f3b4891a527a6f00d16"
      }
    },
    {
      "id": "627d673f4891a527a6efdf3a",
      "app_id": "com.maxmpz.audioplayer",
      "title": "Poweramp  - мощный музыкальный плеер ",
      "short_description": "Poweramp - это мощный аудиоплеер для Андроида. Пробная версия",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/d5809aae2fd1c824575c927c",
      "rating": "4,99",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 14274874,
      "r_count": "",
      "ar": "16+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "10.7тыс.",
      "did": "627999204891a55fa0377207",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 938009,
        "version_name": "build-938-uni",
        "create_at": "2022-05-12T20:44:07.833Z",
        "release_notes": "• пробный период значительно увеличен в связи с отключением Google возможности оплаты\n• новая опция Кнопки внизу списков\n• новая опция Кнопки в заголовке\n• выделение диапазона в списке долгим нажатием\n• новая опция Пауза при выключении экрана",
        "install_path": "https://cdnb.nashstore.ru/store/install/627d71974891a527a6efe000"
      }
    },
    {
      "id": "628257ad4891a569645f12a8",
      "app_id": "com.zvooq.openplay",
      "title": "Звук. Музыка и подкасты",
      "short_description": "Любимая музыка, которую можно скачать и слушать без интернета",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/3a2694ee758aff1185d61aaa",
      "rating": "4,75",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 36664085,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "10.3тыс.",
      "did": "628257624891a569645f06d7",
      "dtitle": "",
      "release": {
        "sdk_min": 25,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 411000101,
        "version_name": "4.11",
        "create_at": "2022-05-16T14:25:30.207Z",
        "release_notes": "Первый релиз в NashStore!",
        "install_path": "https://cdnb.nashstore.ru/store/install/62825eda4891a569646024c5"
      }
    },
    {
      "id": "6284bf240a39b25e4dd69071",
      "app_id": "free.zaycev.net",
      "title": "Zaycev.net: музыка для каждого",
      "short_description": "Современная российская музыка",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/9a391f26215ecad7150e4004",
      "rating": "4,92",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 28154933,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "8.3тыс.",
      "did": "6284bee1fb3ed33a3edb1ea6",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 535,
        "version_name": "7.19.15",
        "create_at": "2022-05-18T11:08:46.176Z",
        "release_notes": "Плейлист дня улучшен! Чем больше слушаешь и скачиваешь, тем лучше плейлист.",
        "install_path": "https://cdnb.nashstore.ru/store/install/6284d3be0a39b25e4dd6cc4d"
      }
    },
    {
      "id": "6283644c4891a5438b388125",
      "app_id": "com.infoshell.recradio",
      "title": "Record Dance Radio",
      "short_description": "Вся танцевальная музыка",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/612c9b2b12150b6a6c992130",
      "rating": "4,92",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 9850228,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "3.3тыс.",
      "did": "628362e24891a5438b386b62",
      "dtitle": "ЗАО \"Радио Рекорд\"",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 196,
        "version_name": "4.1.196",
        "create_at": "2022-05-17T09:21:27.878Z",
        "release_notes": "Исправлен логин в чате со студией\nОптимизирован код\nУскорена работа приложения",
        "install_path": "https://cdnb.nashstore.ru/store/install/628369174891a5438b38cf99"
      }
    },
    {
      "id": "627ee4844891a527a6effac0",
      "app_id": "ru.geedeonradio",
      "title": "Geedeon Radio - Deep House Музыка",
      "short_description": "Deep House, Car Bass или Chill без ограничений. Более 2.000.000 слушателей.",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/deb5c3dc12cd0150093c15b2",
      "rating": "5,00",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 44979574,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "1.1тыс.",
      "did": "627ee4444891a527a6effabf",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 100000140,
        "version_name": "3.3.8",
        "create_at": "2022-05-14T14:49:35.483Z",
        "release_notes": "Новая версия",
        "install_path": "https://cdnb.nashstore.ru/store/install/627fc17f4891a527a6f00858"
      }
    },
    {
      "id": "627b6e174891a5fdaa00e917",
      "app_id": "com.karaokee.app",
      "title": "Караоке - Застольные песни",
      "short_description": "Песни караоке для всей семьи, хиты прошлых лет и даже современных исполнителей!",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/a55b61c28cea649b91a2a387",
      "rating": "5,00",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 10491304,
      "r_count": "",
      "ar": "16+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "339",
      "did": "627b691f4891a5fdaa00e783",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 6,
        "version_name": "1.0.2",
        "create_at": "2022-05-11T08:58:21.511Z",
        "release_notes": "Релиз приложения",
        "install_path": "https://cdnb.nashstore.ru/store/install/627b7aad4891a5fdaa00ec38"
      }
    },
    {
      "id": "628077b94891a527a6f00e85",
      "app_id": "ru.demonapps.onlineradio",
      "title": "Радио Он-Лайн",
      "short_description": "Слушаем радио от \"Кимры гараЖ\"",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/3e6c525e9d17a40eef4e2724",
      "rating": "4,29",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 6850983,
      "r_count": "",
      "ar": "16+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "294",
      "did": "627a87994891a5f7360a75aa",
      "dtitle": "DemonApps",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 32,
        "version_code": 8,
        "version_name": "0.0.8",
        "create_at": "2022-05-15T03:58:15.955Z",
        "release_notes": "Теперь и в NashStore",
        "install_path": "https://cdnb.nashstore.ru/store/install/62807a574891a527a6f00ea2"
      }
    },
    {
      "id": "6278fdae4891a52a3548ae63",
      "app_id": "com.parabola.newtone",
      "title": "Newtone - музыкальный плеер",
      "short_description": "Newtone - это плеер, который позволит Вам по новому слушать любимую музыку",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/af873d7f61573e0e3d2b5481",
      "rating": "4,50",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 4214984,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "183",
      "did": "6278fc974891a52a3548adad",
      "dtitle": "Parabola Development",
      "release": {
        "sdk_min": 16,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 32,
        "version_name": "1.0.7",
        "create_at": "2022-05-09T12:24:20.773Z",
        "release_notes": "Newtone теперь в Nashstore",
        "install_path": "https://cdnb.nashstore.ru/store/install/627907f44891a52a3548b423"
      }
    },
    {
      "id": "627a89c74891a5f7360a762c",
      "app_id": "com.vfm.droid",
      "title": "Vanilla FM Droid",
      "short_description": "Vanilla FM теперь и в твоем Android смартфоне",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/50763d48efbc16445196ec9c",
      "rating": "4,43",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 14223282,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "122",
      "did": "627a89a24891a5f7360a7626",
      "dtitle": "Vanilla Tech",
      "release": {
        "sdk_min": 19,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 20220515,
        "version_name": "1.0",
        "create_at": "2022-05-15T11:48:20.666Z",
        "release_notes": "Станьте первыми, кто опробует приложение Vanilla FM Droid – скачайте первую версию приложения и слушайте наше интернет радио без ограничений и рекламы.",
        "install_path": "https://cdnb.nashstore.ru/store/install/6280e8844891a527a6f0149b"
      }
    },
    {
      "id": "627a6dd74891a5e308a58074",
      "app_id": "com.gourmetlabs.sparkgl747a",
      "title": "Spark GL-747A folder player vintage VU-meter",
      "short_description": "Музыкальный плеер подкаталогов имитирующий знаменитый кассетный бумбокс",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/634a550a5e8732868a0ed5d1",
      "rating": "0.0",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 9572046,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "91",
      "did": "627a6d4d4891a5e308a58059",
      "dtitle": "GourmetLabs",
      "release": {
        "sdk_min": 16,
        "sdk_max": 0,
        "sdk_version": 29,
        "version_code": 11,
        "version_name": "R006",
        "create_at": "2022-05-10T14:14:29.987Z",
        "release_notes": "Целевой API 29 (Android 10), 32-х битная версия.",
        "install_path": "https://cdnb.nashstore.ru/store/install/627a73454891a5e308a581a3"
      }
    },
    {
      "id": "627cf1c04891a5fdaa011796",
      "app_id": "com.dinaraparanid.prima",
      "title": "Prima",
      "short_description": "Музыкальный плеер, в котором есть всё",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/82013619101718119ff418e5",
      "rating": "3,67",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 151815669,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "68",
      "did": "627cf1964891a5fdaa01178e",
      "dtitle": "Paranid5",
      "release": {
        "sdk_min": 23,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 1,
        "version_name": "V 1.1.0.1",
        "create_at": "2022-05-15T17:19:05.669Z",
        "release_notes": "Первый релиз в Nash Store! За полным списком изменений каждой версии сюда: https://github.com/dinaraparanid/PrimaMobile/releases",
        "install_path": "https://cdnb.nashstore.ru/store/install/628136094891a527a6f01a57"
      }
    },
    {
      "id": "6278f7a44891a52a3548aa10",
      "app_id": "com.imabuilder.deryvierstudio.deryviermusic",
      "title": "DERYVIER MUSIC",
      "short_description": "Музыка разных жанров и направлений",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/c3be37906943d5bf2a63c694",
      "rating": "5,00",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 5728737,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "47",
      "did": "6278f6d14891a52a3548a97e",
      "dtitle": "",
      "release": {
        "sdk_min": 19,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 22051600,
        "version_name": "1.220416",
        "create_at": "2022-05-22T10:43:22.509Z",
        "release_notes": "Изменён дизайн страниц альбомов. Обновлена главная страница.",
        "install_path": "https://cdnb.nashstore.ru/store/install/628a13ca0a39b2aa4eaaddfb"
      }
    },
    {
      "id": "627d72724891a527a6efe01f",
      "app_id": "com.spectroanalyz",
      "title": "Measuring Center",
      "short_description": "Приравняет телефон и планшет к профессиональному спетроанализатору!",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/e37c7b7aa039c8b2a60fb193",
      "rating": "5,00",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 39111222,
      "r_count": "",
      "ar": "6+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "30",
      "did": "627d6e9a4891a527a6efdfcd",
      "dtitle": "",
      "release": {
        "sdk_min": 24,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 50,
        "version_name": "2.71",
        "create_at": "2022-05-12T20:55:21.814Z",
        "release_notes": "Версия 2.71",
        "install_path": "https://cdnb.nashstore.ru/store/install/627d74394891a527a6efe037"
      }
    },
    {
      "id": "628257cf4891a569645f188b",
      "app_id": "com.s13.live",
      "title": "Радио s13.live",
      "short_description": "Радио s13.live — онлайн радио из Гродно, работает 24/7.",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/becd80966a70f1d9abec6079",
      "rating": "5,00",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 38149953,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "14",
      "did": "628252574891a569645e2d73",
      "dtitle": "MEGA.BY",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 29,
        "version_code": 1,
        "version_name": "1",
        "create_at": "2022-05-16T14:05:47.095Z",
        "release_notes": "Повышение стабильности и качества вещания",
        "install_path": "https://cdnb.nashstore.ru/store/install/62825a3b4891a569645f78f8"
      }
    },
    {
      "id": "62836d934891a5de4cd6f6aa",
      "app_id": "com.sherdle.webtoapp",
      "title": "Sirena Music",
      "short_description": "Новые ноты каждый день! ",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/c9189a46c58423b069238b42",
      "rating": "0.0",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 5756485,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "2",
      "did": "628277434891a56964627216",
      "dtitle": "",
      "release": {
        "sdk_min": 16,
        "sdk_max": 0,
        "sdk_version": 29,
        "version_code": 1,
        "version_name": "1.0",
        "create_at": "2022-05-17T09:50:45.132Z",
        "release_notes": "Релиз приложения",
        "install_path": "https://cdnb.nashstore.ru/store/install/62836ff54891a5de4cd71a22"
      }
    },
    {
      "id": "628256e94891a569645ef44f",
      "app_id": "ru.zatochisto.radio107fm",
      "title": "Умное Радио",
      "short_description": "Радиостанция из Сарова, вещающая на 107.0Fm",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/73401114ccd1189b2b468c0b",
      "rating": "0.0",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 7119241,
      "r_count": "",
      "ar": "18+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "1",
      "did": "627fa2924891a527a6f00667",
      "dtitle": "djdance",
      "release": {
        "sdk_min": 22,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 5,
        "version_name": "2",
        "create_at": "2022-05-16T14:59:25.461Z",
        "release_notes": "Мы специально обновили приложение - впервые за 2 года, чтобы разместиться новой на российской площадке.",
        "install_path": "https://cdnb.nashstore.ru/store/install/628266cd4891a5696461438b"
      }
    }
  ],
  "status": "success",
  "total": 17
}

```

</details>

## App search

METHOD: GET

URL: "https://store.nashstore.ru/api/mobile/v1/apps/search?page=1&search=&type=game"

<details> 
<summary>Responce:</summary>

```json

{
  "list": [
    {
      "id": "627ba20e4891a5fdaa00f555",
      "app_id": "ru.dublgis.dgismobile",
      "title": "2ГИС - карты и навигатор",
      "short_description": "Карта и справочник городов России. Транспорт и навигация.",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/5077eab7ea55ee7a3d8feee0",
      "rating": "4,90",
      "category": "Карты и навигация",
      "type": "application",
      "size": 170962727,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "115.7тыс.",
      "did": "627ba1574891a5fdaa00f529",
      "dtitle": "2ГИС",
      "release": {
        "sdk_min": 23,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 231000405,
        "version_name": "6.1.0.405.19",
        "create_at": "2022-05-11T11:52:03.93Z",
        "release_notes": "В этом релизе мы внесли улучшения по вашей обратной связи: \n- обучили ассистентов Салют поиску по номерам квартир и подъездов,\n- попросили голосовых ассистентов больше не озвучивать результаты поиска.",
        "install_path": "https://cdnb.nashstore.ru/store/install/627ba3634891a5fdaa00f5af"
      }
    },
    {
      "id": "627fe48c4891a527a6f00a2a",
      "app_id": "ru.rutube.app",
      "title": "Rutube",
      "short_description": "Российский аналог видеохостинг Rutube ",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/d73314c0e7f60acdb59dc72e",
      "rating": "4,64",
      "category": "Видеоплееры и редакторы",
      "type": "application",
      "size": 15909954,
      "r_count": "",
      "ar": "3+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "70.3тыс.",
      "did": "627fe1504891a527a6f00a07",
      "dtitle": "",
      "release": {
        "sdk_min": 19,
        "sdk_max": 0,
        "sdk_version": 29,
        "version_code": 1801001,
        "version_name": "18.1.1-android",
        "create_at": "2022-05-14T17:31:37.564Z",
        "release_notes": "Данный видеохостинг Российский Youtube",
        "install_path": "https://cdnb.nashstore.ru/store/install/627fe7794891a527a6f00a57"
      }
    },
    {
      "id": "62826abb4891a5696461b931",
      "app_id": "com.octopod.russianpost.client.android",
      "title": "Почта России",
      "short_description": "Официальное приложение Почты России",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/53808ecc9efb3019e1002a47",
      "rating": "4,92",
      "category": "Покупки",
      "type": "application",
      "size": 145703094,
      "r_count": "",
      "ar": "6+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "68.9тыс.",
      "did": "62826a894891a5696461b59a",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 782,
        "version_name": "7.8.2",
        "create_at": "2022-05-16T15:43:24.394Z",
        "release_notes": "- Отправляйте документы дешевле с новым тарифом EMS с документами\n- Упростили выбор времени курьерской доставки исходящих EMS-отправлений\n- Добавили оплату ЕMS-отправлений получателем \n- Сделали чат с поддержкой удобнее",
        "install_path": "https://cdnb.nashstore.ru/store/install/6282711c4891a56964622bb7"
      }
    },
    {
      "id": "627cd7524891a5fdaa01146a",
      "app_id": "ru.vtb24.mobilebanking.android",
      "title": "ВТБ Онлайн",
      "short_description": "Мобильное приложение ВТБ Онлайн — это полноценный банк в вашем смартфоне!",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/4cf82e363c510c935a9211c7",
      "rating": "4,89",
      "category": "Банки",
      "type": "application",
      "size": 405385212,
      "r_count": "",
      "ar": "3+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "62.7тыс.",
      "did": "627cd62e4891a5fdaa01144d",
      "dtitle": "VTB Bank, PJSC",
      "release": {
        "sdk_min": 23,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 2090140450,
        "version_name": "16.10.0.0",
        "create_at": "2022-05-19T14:01:16.776Z",
        "release_notes": "Запустили сервис проверки ссылок на фишинг — он поможет защититься от ссылок на мошеннические интернет-ресурсы, например, это могут быть копии сайтов известных компаний. Чтобы проверить ссылку, перейдите в раздел «Услуги» > «Проверка ссылок». \n\nЕще добавили несколько улучшений в чат — там появилась возможность отправлять не только фотографии, но и документы. Кстати, теперь вы можете отправить сразу несколько файлов за один раз.\n\nКоманда ВТБ Онлайн",
        "install_path": "https://cdnb.nashstore.ru/store/install/62864dac0a39b277f96748e2"
      }
    },
    {
      "id": "627b72384891a5fdaa00ea2f",
      "app_id": "ru.alfabank.mobile.android",
      "title": "Альфа-Банк",
      "short_description": "Мобильное приложение Альфа-Банка",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/3748de58743e5e2896ebf322",
      "rating": "4,84",
      "category": "Банки",
      "type": "application",
      "size": 143870795,
      "r_count": "",
      "ar": "3+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "49.8тыс.",
      "did": "627b71f94891a5fdaa00ea1f",
      "dtitle": "Альфа-Банк",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 2036115116,
        "version_name": "11.51.16",
        "create_at": "2022-05-11T12:36:33.855Z",
        "release_notes": "В этом обновлении, через раздел Справки и выписки в профиле или витрине, можно заказать справку для госслужащих за отчетный период 2021 года. Справка формируется онлайн — показывает информацию о доходах, расходах, имуществе и обязательствах. В приложении Альфа-Банка справка приходит моментально. Также в приложении появилось автоматическое открытие накопительного счета при заказе и выдаче дебетовой карты.",
        "install_path": "https://cdnb.nashstore.ru/store/install/627badd14891a5fdaa00f7f0"
      }
    },
    {
      "id": "627e135e4891a527a6efeabf",
      "app_id": "ru.instamart",
      "title": "СберМаркет: Доставка продуктов",
      "short_description": "СберМаркет - это крупнейший сервис доставки из магазинов в России. ",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/53c1d35d8a7941c0fdc25a01",
      "rating": "4,79",
      "category": "Еда и напитки",
      "type": "application",
      "size": 159247617,
      "r_count": "",
      "ar": "3+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "34.9тыс.",
      "did": "627e11864891a527a6efea70",
      "dtitle": "СберМаркет: Доставка продуктов",
      "release": {
        "sdk_min": 23,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 11877451,
        "version_name": "6.22.7 (11877451)",
        "create_at": "2022-05-13T12:44:01.445Z",
        "release_notes": "Первый релиз в NashStore!",
        "install_path": "https://cdnb.nashstore.ru/store/install/627e52914891a527a6eff102"
      }
    },
    {
      "id": "627cfb064891a5fdaa01192a",
      "app_id": "ru.getpharma.eapteka",
      "title": "Еаптека",
      "short_description": "Интернет-аптека с доставкой лекарств и витаминов на дом. Скидка на первый заказ.",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/e9ca3e272424df7c216ee47f",
      "rating": "4,91",
      "category": "Медицина",
      "type": "application",
      "size": 95494863,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "28.2тыс.",
      "did": "627cd3564891a5fdaa0113ea",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 371,
        "version_name": "22.4.2",
        "create_at": "2022-05-12T14:05:20.351Z",
        "release_notes": "1. Программа лояльности\nЛичный кабинет заработал в полную силу: в нём можно увидеть состояние бонусного счёта и историю операций.\n2. Сроки доставки\nВы сможете увидеть ближайший интервал доставки до того, как начнёте оформлять заказ — мы привязали его к адресу.\n3. Акции\nПереработали страницу акций: теперь можно быстро переключаться между актуальными и завершёнными предложениями. \n\nРасскажите, как вам эта версия? Мы готовы к любой обратной связи и будем рады, если вы напишете на mobile@eapteka.ru.",
        "install_path": "https://cdnb.nashstore.ru/store/install/627d14204891a5fdaa011c9a"
      }
    },
    {
      "id": "627d03024891a5fdaa011a8e",
      "app_id": "com.vgtrk.smotrim",
      "title": "СМОТРИМ. Россия, ТВ и радио",
      "short_description": "Новости, ток-шоу, фильмы, мультфильмы, подкасты - все в одном приложении!",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/7a07c4b7bce8e4ce9c511a26",
      "rating": "4,71",
      "category": "Развлечения",
      "type": "application",
      "size": 45432234,
      "r_count": "",
      "ar": "18+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "27.9тыс.",
      "did": "627d02dc4891a5fdaa011a8a",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 80409,
        "version_name": "8.4",
        "create_at": "2022-05-12T14:05:00.504Z",
        "release_notes": "Внесли некоторые улучшения и поработали над ошибками, чтобы вам было удобнее пользоваться приложением.",
        "install_path": "https://cdnb.nashstore.ru/store/install/627d140c4891a5fdaa011c99"
      }
    },
    {
      "id": "627a5dbd4891a5e308a57d5b",
      "app_id": "ru.rt.video.app.mobile",
      "title": "Wink – ТВ, фильмы, сериалы",
      "short_description": "Смотри в Wink онлайн фильмы, сериалы, мультфильмы и ТВ каналы",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/547ca89e526f6986bad5f6c2",
      "rating": "4,82",
      "category": "Развлечения",
      "type": "application",
      "size": 13868616,
      "r_count": "",
      "ar": "3+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "25.9тыс.",
      "did": "627a5d1e4891a5d48ed2cdf4",
      "dtitle": "Wink",
      "release": {
        "sdk_min": 24,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 138100,
        "version_name": "1.38.1",
        "create_at": "2022-05-10T12:51:59.789Z",
        "release_notes": "В новой версии просмотр стал комфортнее - мы исправили множество ошибок. При случайных наклонах телефона плеер больше не сворачивается, а место последнего просмотра сохраняется всегда.\n\nПолностью переработали механику покупок, оптимизировали приложение и устранили ошибки из предыдущих версий",
        "install_path": "https://cdnb.nashstore.ru/store/install/627a5fef4891a5e308a57dcc"
      }
    },
    {
      "id": "62801c234891a527a6f00cfe",
      "app_id": "com.aimp.player",
      "title": "AIMP",
      "short_description": "Это аудиоплеер на основе плейлистов для платформы Android",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/e4954fb66d98e2a01e9662c9",
      "rating": "4,93",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 11583352,
      "r_count": "",
      "ar": "6+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "23.1тыс.",
      "did": "62801b6c4891a527a6f00cec",
      "dtitle": "Artem Izmaylov",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 1193,
        "version_name": "v3.22, build 1193 (26.04.2022)",
        "create_at": "2022-05-14T21:29:31.777Z",
        "release_notes": "Первый публичный релиз на платформе",
        "install_path": "https://cdnb.nashstore.ru/store/install/62801f3b4891a527a6f00d16"
      }
    },
    {
      "id": "627bbf134891a5fdaa00fb93",
      "app_id": "ru.sovcomcard.halva.v1",
      "title": "Халва - Совкомбанк",
      "short_description": "Приложение «Халва – Совкомбанк» — это банковский офис на экране смартфона!",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/d7a96b646e3d0bd83e9dd58a",
      "rating": "4,76",
      "category": "Банки",
      "type": "application",
      "size": 107146617,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "20.9тыс.",
      "did": "627bbe634891a5fdaa00fb76",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 110145600,
        "version_name": "6.6.2",
        "create_at": "2022-05-11T14:33:55.337Z",
        "release_notes": "Приложение «Халва – Совкомбанк» — это банковский офис на экране смартфона!",
        "install_path": "https://cdnb.nashstore.ru/store/install/627bc9534891a5fdaa00fd33"
      }
    },
    {
      "id": "627acc554891a5fdaa00d22c",
      "app_id": "ru.stoloto.mobile",
      "title": "Столото",
      "short_description": "Государственные лотереи",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/4780ea2d7cb57d7f59aab8c0",
      "rating": "4,59",
      "category": "Развлечения",
      "type": "application",
      "size": 40265681,
      "r_count": "",
      "ar": "18+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "19.6тыс.",
      "did": "627ab60f4891a5fdaa00cea5",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 3783,
        "version_name": "14.4.1",
        "create_at": "2022-05-10T20:45:55.348Z",
        "release_notes": "Встречайте — официальное приложение «Столото» для Android! Играйте в популярные государственные лотереи, легко проверяйте розничные билеты, следите за тиражными предложениями и специальными акциями.",
        "install_path": "https://cdnb.nashstore.ru/store/install/627acf034891a5fdaa00d287"
      }
    },
    {
      "id": "627e42174891a527a6efefa1",
      "app_id": "mobi.zona",
      "title": "Zona",
      "short_description": "Бесплатный онлайн-кинотеатр Zona (Зона)",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/7a71b8ca555184a73fb5e941",
      "rating": "4,92",
      "category": "Развлечения",
      "type": "application",
      "size": 8369332,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "16.1тыс.",
      "did": "627e41f24891a527a6efefa0",
      "dtitle": "",
      "release": {
        "sdk_min": 17,
        "sdk_max": 0,
        "sdk_version": 32,
        "version_code": 135,
        "version_name": "2.0.60",
        "create_at": "2022-05-13T12:04:59.272Z",
        "release_notes": "Добавлены новые источники видео",
        "install_path": "https://cdnb.nashstore.ru/store/install/627e496b4891a527a6eff038"
      }
    },
    {
      "id": "627b70194891a5fdaa00e9a4",
      "app_id": "ru.abrr.gas",
      "title": "Мой ГАЗ",
      "short_description": "Оплата за газ становится проще и удобнее.",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/e744c7d69af5654da24e5db7",
      "rating": "4,80",
      "category": "Бизнес",
      "type": "application",
      "size": 35732092,
      "r_count": "",
      "ar": "16+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "11.6тыс.",
      "did": "627b6ccd4891a5fdaa00e8a8",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 226,
        "version_name": "6.6.26",
        "create_at": "2022-05-11T09:03:04.336Z",
        "release_notes": "Первый выпуск приложения Мой ГАЗ в сервисе Nashstore",
        "install_path": "https://cdnb.nashstore.ru/store/install/627b7bc84891a5fdaa00ec86"
      }
    },
    {
      "id": "627e12e84891a527a6efeaa9",
      "app_id": "logo.com.mbanking",
      "title": "ПСБ",
      "short_description": "Мобильный. Удобный. Сделан с любовью",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/0a67ecf31d6a61ebfe310702",
      "rating": "4,86",
      "category": "Банки",
      "type": "application",
      "size": 99982046,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "11.1тыс.",
      "did": "627e0c964891a527a6efe9a9",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 338,
        "version_name": "3.53.3",
        "create_at": "2022-05-18T03:56:35.278Z",
        "release_notes": "С каждым обновлением стараемся делать приложение удобнее. \n\nЧто нового в этой версии:\n\n1. Владельцы Android могут привязать свои карты Мир к сервису «Mir Pay» в один клик.\n2. Теперь можно легко узнать реквизиты любой своей карты, а не только виртуальной.\n3. Страховые полисы «Автопомощь» отображаются сразу на главном экране мобильного банка.\n\nДайте знать, насколько удобно пользоваться новым функционалом: оставляйте отзывы и комментарии.",
        "install_path": "https://cdnb.nashstore.ru/store/install/62846e730a39b254006f35a1"
      }
    },
    {
      "id": "627d673f4891a527a6efdf3a",
      "app_id": "com.maxmpz.audioplayer",
      "title": "Poweramp  - мощный музыкальный плеер ",
      "short_description": "Poweramp - это мощный аудиоплеер для Андроида. Пробная версия",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/d5809aae2fd1c824575c927c",
      "rating": "4,99",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 14274874,
      "r_count": "",
      "ar": "16+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "10.7тыс.",
      "did": "627999204891a55fa0377207",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 938009,
        "version_name": "build-938-uni",
        "create_at": "2022-05-12T20:44:07.833Z",
        "release_notes": "• пробный период значительно увеличен в связи с отключением Google возможности оплаты\n• новая опция Кнопки внизу списков\n• новая опция Кнопки в заголовке\n• выделение диапазона в списке долгим нажатием\n• новая опция Пауза при выключении экрана",
        "install_path": "https://cdnb.nashstore.ru/store/install/627d71974891a527a6efe000"
      }
    },
    {
      "id": "628257ad4891a569645f12a8",
      "app_id": "com.zvooq.openplay",
      "title": "Звук. Музыка и подкасты",
      "short_description": "Любимая музыка, которую можно скачать и слушать без интернета",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/3a2694ee758aff1185d61aaa",
      "rating": "4,75",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 36664085,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "10.3тыс.",
      "did": "628257624891a569645f06d7",
      "dtitle": "",
      "release": {
        "sdk_min": 25,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 411000101,
        "version_name": "4.11",
        "create_at": "2022-05-16T14:25:30.207Z",
        "release_notes": "Первый релиз в NashStore!",
        "install_path": "https://cdnb.nashstore.ru/store/install/62825eda4891a569646024c5"
      }
    },
    {
      "id": "628215ed4891a5abaeee3072",
      "app_id": "ru.vtb.invest",
      "title": "ВТБ Мои инвестиции",
      "short_description": "ВТБ Мои Инвестиции — ваш личный помощник по торговле на бирже в смартфоне",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/063780134774e33cd390a84e",
      "rating": "4,93",
      "category": "Финансы",
      "type": "application",
      "size": 102584373,
      "r_count": "",
      "ar": "3+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "9.9тыс.",
      "did": "628215d44891a5abaeee3049",
      "dtitle": "Банк ВТБ (ПАО)",
      "release": {
        "sdk_min": 23,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 31428000,
        "version_name": "2.28.1-production",
        "create_at": "2022-05-16T12:10:04.081Z",
        "release_notes": "— Теперь пополнить счет можно в любое время с карты любого банка.\n\n— На карточке актива в разделе «Обзор» теперь отображается, структурный это продукт или нет.",
        "install_path": "https://cdnb.nashstore.ru/store/install/62823f1c4891a53482334f03"
      }
    },
    {
      "id": "6281eb2b4891a568e11a2be7",
      "app_id": "ru.myauchan.droid",
      "title": "Мой АШАН",
      "short_description": "Все акции и скидки сети АШАН, новая программа лояльности, доставка продуктов",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/43d0e38882e3fd35013a250b",
      "rating": "5,00",
      "category": "Покупки",
      "type": "application",
      "size": 46647143,
      "r_count": "",
      "ar": "0+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "8.5тыс.",
      "did": "6281eb0f4891a568e11a2bdb",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 30,
        "version_code": 3028,
        "version_name": "3.2.8",
        "create_at": "2022-05-18T10:20:42.842Z",
        "release_notes": "Повышена безопасность и стабильность работы приложения.",
        "install_path": "https://cdnb.nashstore.ru/store/install/6284c87a0a39b25e4dd6a9dd"
      }
    },
    {
      "id": "6284bf240a39b25e4dd69071",
      "app_id": "free.zaycev.net",
      "title": "Zaycev.net: музыка для каждого",
      "short_description": "Современная российская музыка",
      "icon": "https://cdnb.nashstore.ru/api/v1/media/9a391f26215ecad7150e4004",
      "rating": "4,92",
      "category": "Музыка и аудио",
      "type": "application",
      "size": 28154933,
      "r_count": "",
      "ar": "12+",
      "ard": "",
      "arl": "https://store.nashstore.ru/rules/age_restrictions",
      "installs": "8.3тыс.",
      "did": "6284bee1fb3ed33a3edb1ea6",
      "dtitle": "",
      "release": {
        "sdk_min": 21,
        "sdk_max": 0,
        "sdk_version": 31,
        "version_code": 535,
        "version_name": "7.19.15",
        "create_at": "2022-05-18T11:08:46.176Z",
        "release_notes": "Плейлист дня улучшен! Чем больше слушаешь и скачиваешь, тем лучше плейлист.",
        "install_path": "https://cdnb.nashstore.ru/store/install/6284d3be0a39b25e4dd6cc4d"
      }
    }
  ],
  "status": "success",
  "total": 986
}

```

</details>

## Main page

METHOD: GET

URL: "https://store.nashstore.ru/api/mobile/v1/selections/main"

<details>
    <summary>Responce:</summary>

```json

{
  "categories": [
    {
      "id": 2,
      "title": "Автомобили и транспорт",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 54
    },
    {
      "id": 3,
      "title": "Банки",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 20
    },
    {
      "id": 4,
      "title": "Бизнес",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app4.png",
      "count": 50
    },
    {
      "id": 5,
      "title": "Видеоплееры и редакторы",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 4
    },
    {
      "id": 6,
      "title": "Дополненная реальность",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app6.png",
      "count": 2
    },
    {
      "id": 7,
      "title": "Еда и напитки",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app7.png",
      "count": 18
    },
    {
      "id": 8,
      "title": "Жилье и дом",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 20
    },
    {
      "id": 9,
      "title": "Здоровье и фитнес",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app9.png",
      "count": 23
    },
    {
      "id": 10,
      "title": "Знакомства",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 14
    },
    {
      "id": 11,
      "title": "Инструменты",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app11.png",
      "count": 60
    },
    {
      "id": 12,
      "title": "Искусство и дизайн",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app12.png",
      "count": 2
    },
    {
      "id": 13,
      "title": "Карты и навигация",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app13.png",
      "count": 11
    },
    {
      "id": 14,
      "title": "Книги и справочники",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app14.png",
      "count": 45
    },
    {
      "id": 15,
      "title": "Комиксы",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app15.png",
      "count": 1
    },
    {
      "id": 16,
      "title": "Красота",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 5
    },
    {
      "id": 17,
      "title": "Материнство и детство",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app17.png",
      "count": 6
    },
    {
      "id": 18,
      "title": "Медицина",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app18.png",
      "count": 14
    },
    {
      "id": 19,
      "title": "Мероприятия",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 5
    },
    {
      "id": 20,
      "title": "Музыка и аудио",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app20.png",
      "count": 17
    },
    {
      "id": 21,
      "title": "Новости и журналы",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 16
    },
    {
      "id": 22,
      "title": "Образование",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app22.png",
      "count": 55
    },
    {
      "id": 23,
      "title": "Персонализация",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 15
    },
    {
      "id": 24,
      "title": "Погода",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app24.png",
      "count": 3
    },
    {
      "id": 25,
      "title": "Покупки",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app25.png",
      "count": 24
    },
    {
      "id": 26,
      "title": "Путешествия",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app26.png",
      "count": 22
    },
    {
      "id": 27,
      "title": "Работа",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app27.png",
      "count": 24
    },
    {
      "id": 28,
      "title": "Развлечения",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app28.png",
      "count": 51
    },
    {
      "id": 29,
      "title": "Связь",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app29.png",
      "count": 14
    },
    {
      "id": 30,
      "title": "Социальные",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app30.png",
      "count": 37
    },
    {
      "id": 31,
      "title": "Спорт",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app31.png",
      "count": 14
    },
    {
      "id": 32,
      "title": "Стиль жизни",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app32.png",
      "count": 11
    },
    {
      "id": 33,
      "title": "Финансы",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app33.png",
      "count": 34
    },
    {
      "id": 34,
      "title": "Фотография",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/app34.png",
      "count": 4
    },
    {
      "id": 35,
      "title": "Другие",
      "type": "application",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/other.png",
      "count": 8
    },
    {
      "id": 1,
      "title": "Аниме",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game1.png",
      "count": 3
    },
    {
      "id": 2,
      "title": "Аркады",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game2.png",
      "count": 37
    },
    {
      "id": 3,
      "title": "Викторины",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game3.png",
      "count": 10
    },
    {
      "id": 4,
      "title": "Военные",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game4.png",
      "count": 2
    },
    {
      "id": 5,
      "title": "Головоломки",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game5.png",
      "count": 42
    },
    {
      "id": 6,
      "title": "Гонки",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game6.png",
      "count": 5
    },
    {
      "id": 7,
      "title": "Детские",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game7.png",
      "count": 11
    },
    {
      "id": 9,
      "title": "Инди",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game9.png",
      "count": 8
    },
    {
      "id": 11,
      "title": "Казуальные",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game11.png",
      "count": 22
    },
    {
      "id": 12,
      "title": "Карточные",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game12.png",
      "count": 11
    },
    {
      "id": 13,
      "title": "Квесты",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game13.png",
      "count": 1
    },
    {
      "id": 14,
      "title": "Логические",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game14.png",
      "count": 7
    },
    {
      "id": 15,
      "title": "Музыка",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game15.png",
      "count": 1
    },
    {
      "id": 16,
      "title": "Настольные игры",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game16.png",
      "count": 15
    },
    {
      "id": 17,
      "title": "Обучающие",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game17.png",
      "count": 5
    },
    {
      "id": 19,
      "title": "Приключения",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game19.png",
      "count": 17
    },
    {
      "id": 20,
      "title": "Ролевые",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game20.png",
      "count": 6
    },
    {
      "id": 21,
      "title": "Российские",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game21.png",
      "count": 4
    },
    {
      "id": 22,
      "title": "Симуляторы",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game22.png",
      "count": 23
    },
    {
      "id": 23,
      "title": "Словесные игры",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game23.png",
      "count": 16
    },
    {
      "id": 24,
      "title": "Спортивные игры",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game24.png",
      "count": 2
    },
    {
      "id": 25,
      "title": "Стратегии",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game25.png",
      "count": 6
    },
    {
      "id": 27,
      "title": "Фэнтези",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game27.png",
      "count": 1
    },
    {
      "id": 28,
      "title": "Шутеры",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game28.png",
      "count": 11
    },
    {
      "id": 29,
      "title": "Экшены",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game29.png",
      "count": 7
    },
    {
      "id": 30,
      "title": "MMORPG",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game30.png",
      "count": 2
    },
    {
      "id": 31,
      "title": "MOBA",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game31.png",
      "count": 1
    },
    {
      "id": 100,
      "title": "Другие",
      "type": "game",
      "icon": "https://cdnb.nashstore.ru/assets/images/app_icons/game100.png",
      "count": 5
    }
  ],
  "limit": 10,
  "list": {
    "1": [
      {
        "id": "6281ab354891a55c611ecaf6",
        "title": "Рекомендации",
        "position": "1",
        "type": "selection_install",
        "description": "Собрали для Вас самое полезное",
        "icon": "",
        "cover": "",
        "apps": [
          {
            "id": "628b61850a39b2beaf6a9b9d",
            "app_id": "ru.ria.ria",
            "title": "РИА Новости",
            "short_description": "Новости России и мира, радио, видео, инфографика от лидера новостного рынка.",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/9970966840d0a0831dd3d855",
            "rating": "0.0",
            "category": "Новости и журналы",
            "type": "application",
            "size": 24140956,
            "r_count": "",
            "ar": "12+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "114",
            "did": "628b60e20a39b2beaf6a9acc",
            "dtitle": "МИА «Россия сегодня»",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 29,
              "version_name": "1.0.29",
              "create_at": "2022-05-23T10:42:47.596Z",
              "release_notes": "Несколько незначительных исправлений",
              "install_path": "https://cdnb.nashstore.ru/store/install/628b6527fb3ed39b22bc1b31"
            }
          },
          {
            "id": "627ba20e4891a5fdaa00f555",
            "app_id": "ru.dublgis.dgismobile",
            "title": "2ГИС - карты и навигатор",
            "short_description": "Карта и справочник городов России. Транспорт и навигация.",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/5077eab7ea55ee7a3d8feee0",
            "rating": "4,90",
            "category": "Карты и навигация",
            "type": "application",
            "size": 170962727,
            "r_count": "",
            "ar": "0+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "115.7тыс.",
            "did": "627ba1574891a5fdaa00f529",
            "dtitle": "2ГИС",
            "release": {
              "sdk_min": 23,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 231000405,
              "version_name": "6.1.0.405.19",
              "create_at": "2022-05-11T11:52:03.93Z",
              "release_notes": "В этом релизе мы внесли улучшения по вашей обратной связи: \n- обучили ассистентов Салют поиску по номерам квартир и подъездов,\n- попросили голосовых ассистентов больше не озвучивать результаты поиска.",
              "install_path": "https://cdnb.nashstore.ru/store/install/627ba3634891a5fdaa00f5af"
            }
          },
          {
            "id": "627cd7524891a5fdaa01146a",
            "app_id": "ru.vtb24.mobilebanking.android",
            "title": "ВТБ Онлайн",
            "short_description": "Мобильное приложение ВТБ Онлайн — это полноценный банк в вашем смартфоне!",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/4cf82e363c510c935a9211c7",
            "rating": "4,89",
            "category": "Банки",
            "type": "application",
            "size": 405385212,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "62.7тыс.",
            "did": "627cd62e4891a5fdaa01144d",
            "dtitle": "VTB Bank, PJSC",
            "release": {
              "sdk_min": 23,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 2090140450,
              "version_name": "16.10.0.0",
              "create_at": "2022-05-19T14:01:16.776Z",
              "release_notes": "Запустили сервис проверки ссылок на фишинг — он поможет защититься от ссылок на мошеннические интернет-ресурсы, например, это могут быть копии сайтов известных компаний. Чтобы проверить ссылку, перейдите в раздел «Услуги» > «Проверка ссылок». \n\nЕще добавили несколько улучшений в чат — там появилась возможность отправлять не только фотографии, но и документы. Кстати, теперь вы можете отправить сразу несколько файлов за один раз.\n\nКоманда ВТБ Онлайн",
              "install_path": "https://cdnb.nashstore.ru/store/install/62864dac0a39b277f96748e2"
            }
          },
          {
            "id": "6284bf240a39b25e4dd69071",
            "app_id": "free.zaycev.net",
            "title": "Zaycev.net: музыка для каждого",
            "short_description": "Современная российская музыка",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/9a391f26215ecad7150e4004",
            "rating": "4,92",
            "category": "Музыка и аудио",
            "type": "application",
            "size": 28154933,
            "r_count": "",
            "ar": "12+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "8.3тыс.",
            "did": "6284bee1fb3ed33a3edb1ea6",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 535,
              "version_name": "7.19.15",
              "create_at": "2022-05-18T11:08:46.176Z",
              "release_notes": "Плейлист дня улучшен! Чем больше слушаешь и скачиваешь, тем лучше плейлист.",
              "install_path": "https://cdnb.nashstore.ru/store/install/6284d3be0a39b25e4dd6cc4d"
            }
          },
          {
            "id": "62833b704891a5438b35d24a",
            "app_id": "com.openbank.msb",
            "title": "Бизнес-портал",
            "short_description": "Бизнес-портал в мобильном приложении ",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/1075e254c2e6b87d4ed0275f",
            "rating": "5,00",
            "category": "Банки",
            "type": "application",
            "size": 32905253,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "227",
            "did": "62833b334891a5438b35d048",
            "dtitle": "ПАО Банк \"ФК Открытие\"",
            "release": {
              "sdk_min": 23,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 617,
              "version_name": "3.24.5",
              "create_at": "2022-05-17T06:53:13.469Z",
              "release_notes": "- добавили возможность отозвать платеж в приложении\n- теперь вы точно не пропустите предложение по кредиту - придет PUSH-уведомление\n- исправили мелкие ошибки для более стабильной работы приложения",
              "install_path": "https://cdnb.nashstore.ru/store/install/628346594891a5438b369a45"
            }
          },
          {
            "id": "627b85ee4891a5fdaa00eebf",
            "app_id": "com.sashadeafstudio.vestifm",
            "title": "Вести ФМ Радио",
            "short_description": "Слушайте русское радио Вести ФМ, последние новости о России",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/60bb8d2422b6a2cc35cb31f5",
            "rating": "5,00",
            "category": "Новости и журналы",
            "type": "application",
            "size": 6462120,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "529",
            "did": "627b84194891a5fdaa00ee61",
            "dtitle": "НашаСтанция",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 16,
              "version_name": "1.5",
              "create_at": "2022-05-11T10:00:08.042Z",
              "release_notes": "Тёмная тема, экономия трафика 32 кбит/с",
              "install_path": "https://cdnb.nashstore.ru/store/install/627b89284891a5fdaa00efa4"
            }
          },
          {
            "id": "628769210a39b2899518d45a",
            "app_id": "ru.ntv.today",
            "title": "Сегодня",
            "short_description": "Новости и не только",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/2015d6a75c7303107efad08f",
            "rating": "0.0",
            "category": "Новости и журналы",
            "type": "application",
            "size": 16264658,
            "r_count": "",
            "ar": "16+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "102",
            "did": "627cc85d4891a5fdaa0112a7",
            "dtitle": "НТВ",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 360,
              "version_name": "2.1.0",
              "create_at": "2022-05-20T15:09:21.306Z",
              "release_notes": "В этой версии:\n- Обновили способы авторизации; \n- Исправили известные краши; \n- Доработали открытие гиперссылок внутри материалов; \n- Привели все экраны в соответствие с общей цветовой схемой.",
              "install_path": "https://cdnb.nashstore.ru/store/install/6287af21fb3ed3663eb580b7"
            }
          },
          {
            "id": "62826be84891a5696461ce94",
            "app_id": "tv.ntvplus.app",
            "title": "НТВ-ПЛЮС ТВ",
            "short_description": "Ваше телевидение на экране смартфона: смотрите кино, мультфильмы, футбол онлайн",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/bcac96ad44499abca6272081",
            "rating": "4,50",
            "category": "Развлечения",
            "type": "application",
            "size": 15581013,
            "r_count": "",
            "ar": "18+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "654",
            "did": "62826b6b4891a5696461c5c1",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 1302387,
              "version_name": "3.8.0",
              "create_at": "2022-05-17T13:51:04.11Z",
              "release_notes": "В этом обновлении:\n\n- В версии для смартфонов и планшетов добавлена поддержка тёмной темы.\n- В международной версии добавлен раздел \"Радио\" (для доступа к прослушиванию нужна авторизация).\n- В разделе ТВ добавлен детский канал \"СуперГерои\".\n- Исправлены мелкие замечания для улучшения работы.\n\nСпасибо, что пользуетесь приложением НТВ-ПЛЮС ТВ! Ждём ваших отзывов и комментариев в Google Play и на support@ntvplus.tv.",
              "install_path": "https://cdnb.nashstore.ru/store/install/6283a8484891a51c52dc36ba"
            }
          },
          {
            "id": "6281eb2b4891a568e11a2be7",
            "app_id": "ru.myauchan.droid",
            "title": "Мой АШАН",
            "short_description": "Все акции и скидки сети АШАН, новая программа лояльности, доставка продуктов",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/43d0e38882e3fd35013a250b",
            "rating": "5,00",
            "category": "Покупки",
            "type": "application",
            "size": 46647143,
            "r_count": "",
            "ar": "0+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "8.4тыс.",
            "did": "6281eb0f4891a568e11a2bdb",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 3028,
              "version_name": "3.2.8",
              "create_at": "2022-05-18T10:20:42.842Z",
              "release_notes": "Повышена безопасность и стабильность работы приложения.",
              "install_path": "https://cdnb.nashstore.ru/store/install/6284c87a0a39b25e4dd6a9dd"
            }
          }
        ]
      }
    ],
    "2": [
      {
        "id": "6281b0404891a55c611ecafd",
        "title": "Медиа",
        "position": "2",
        "type": "promo",
        "description": "Онлайн-кинотеатры и СМИ",
        "icon": "https://cdnb.nashstore.ru/api/v1/media/4718263ceb504f3fd9a8695e",
        "cover": "https://cdnb.nashstore.ru/api/v1/media/789197393e8839551d7c3599",
        "apps": [
          {
            "id": "627a5dbd4891a5e308a57d5b",
            "app_id": "ru.rt.video.app.mobile",
            "title": "Wink – ТВ, фильмы, сериалы",
            "short_description": "Смотри в Wink онлайн фильмы, сериалы, мультфильмы и ТВ каналы",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/547ca89e526f6986bad5f6c2",
            "rating": "4,82",
            "category": "Развлечения",
            "type": "application",
            "size": 13868616,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "25.9тыс.",
            "did": "627a5d1e4891a5d48ed2cdf4",
            "dtitle": "Wink",
            "release": {
              "sdk_min": 24,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 138100,
              "version_name": "1.38.1",
              "create_at": "2022-05-10T12:51:59.789Z",
              "release_notes": "В новой версии просмотр стал комфортнее - мы исправили множество ошибок. При случайных наклонах телефона плеер больше не сворачивается, а место последнего просмотра сохраняется всегда.\n\nПолностью переработали механику покупок, оптимизировали приложение и устранили ошибки из предыдущих версий",
              "install_path": "https://cdnb.nashstore.ru/store/install/627a5fef4891a5e308a57dcc"
            }
          },
          {
            "id": "627fe48c4891a527a6f00a2a",
            "app_id": "ru.rutube.app",
            "title": "Rutube",
            "short_description": "Российский аналог видеохостинг Rutube ",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/d73314c0e7f60acdb59dc72e",
            "rating": "4,64",
            "category": "Видеоплееры и редакторы",
            "type": "application",
            "size": 15909954,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "70.3тыс.",
            "did": "627fe1504891a527a6f00a07",
            "dtitle": "",
            "release": {
              "sdk_min": 19,
              "sdk_max": 0,
              "sdk_version": 29,
              "version_code": 1801001,
              "version_name": "18.1.1-android",
              "create_at": "2022-05-14T17:31:37.564Z",
              "release_notes": "Данный видеохостинг Российский Youtube",
              "install_path": "https://cdnb.nashstore.ru/store/install/627fe7794891a527a6f00a57"
            }
          },
          {
            "id": "62826be84891a5696461ce94",
            "app_id": "tv.ntvplus.app",
            "title": "НТВ-ПЛЮС ТВ",
            "short_description": "Ваше телевидение на экране смартфона: смотрите кино, мультфильмы, футбол онлайн",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/bcac96ad44499abca6272081",
            "rating": "4,50",
            "category": "Развлечения",
            "type": "application",
            "size": 15581013,
            "r_count": "",
            "ar": "18+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "654",
            "did": "62826b6b4891a5696461c5c1",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 1302387,
              "version_name": "3.8.0",
              "create_at": "2022-05-17T13:51:04.11Z",
              "release_notes": "В этом обновлении:\n\n- В версии для смартфонов и планшетов добавлена поддержка тёмной темы.\n- В международной версии добавлен раздел \"Радио\" (для доступа к прослушиванию нужна авторизация).\n- В разделе ТВ добавлен детский канал \"СуперГерои\".\n- Исправлены мелкие замечания для улучшения работы.\n\nСпасибо, что пользуетесь приложением НТВ-ПЛЮС ТВ! Ждём ваших отзывов и комментариев в Google Play и на support@ntvplus.tv.",
              "install_path": "https://cdnb.nashstore.ru/store/install/6283a8484891a51c52dc36ba"
            }
          },
          {
            "id": "6284fb4cfb3ed33c3ebf2cc8",
            "app_id": "limehd.ru.ctv",
            "title": "Цифровое ТВ: 20 каналов онлайн",
            "short_description": "Цифровое ТВ (20 каналов цифровых мультиплексов) на твоем смартфоне.",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/eaa8b1aa4a1c06998dfc8ed1",
            "rating": "4,97",
            "category": "Развлечения",
            "type": "application",
            "size": 24694891,
            "r_count": "",
            "ar": "12+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "4.7тыс.",
            "did": "628264464891a5696460eabf",
            "dtitle": "Лайм Эйч Ди",
            "release": {
              "sdk_min": 19,
              "sdk_max": 0,
              "sdk_version": 32,
              "version_code": 259,
              "version_name": "2.5.7N",
              "create_at": "2022-05-19T14:48:53.872Z",
              "release_notes": "Смотрите более 30 самых популярных ТВ-каналов бесплатно",
              "install_path": "https://cdnb.nashstore.ru/store/install/628658d5fb3ed3501d52ea66"
            }
          },
          {
            "id": "627e7b194891a527a6eff48b",
            "app_id": "com.gsgroup.tricoloronline.mobile",
            "title": "Триколор Кино и ТВ",
            "short_description": "Смотрите фильмы, сериалы и ТВ-каналы от Триколора бесплатно.",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/c47e57d8058115cbe17ec9a4",
            "rating": "4,90",
            "category": "Развлечения",
            "type": "application",
            "size": 15476095,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "6.6тыс.",
            "did": "627e78bb4891a527a6eff454",
            "dtitle": "НАО «Национальная спутниковая компания»",
            "release": {
              "sdk_min": 23,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 2022200,
              "version_name": "2.2.2200",
              "create_at": "2022-05-16T16:36:32.669Z",
              "release_notes": "В предвкушении весны хочется перемен. Мы обновились и стали еще удобнее. Всю необходимую информацию теперь можно найти сразу в приложении: подключать и управлять подписками, проверять состояние и список услуг.\n\nГотовимся к теплому сезону, ваш Триколор",
              "install_path": "https://cdnb.nashstore.ru/store/install/62827d904891a5696462df95"
            }
          },
          {
            "id": "628769210a39b2899518d45a",
            "app_id": "ru.ntv.today",
            "title": "Сегодня",
            "short_description": "Новости и не только",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/2015d6a75c7303107efad08f",
            "rating": "0.0",
            "category": "Новости и журналы",
            "type": "application",
            "size": 16264658,
            "r_count": "",
            "ar": "16+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "102",
            "did": "627cc85d4891a5fdaa0112a7",
            "dtitle": "НТВ",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 360,
              "version_name": "2.1.0",
              "create_at": "2022-05-20T15:09:21.306Z",
              "release_notes": "В этой версии:\n- Обновили способы авторизации; \n- Исправили известные краши; \n- Доработали открытие гиперссылок внутри материалов; \n- Привели все экраны в соответствие с общей цветовой схемой.",
              "install_path": "https://cdnb.nashstore.ru/store/install/6287af21fb3ed3663eb580b7"
            }
          },
          {
            "id": "627b85ee4891a5fdaa00eebf",
            "app_id": "com.sashadeafstudio.vestifm",
            "title": "Вести ФМ Радио",
            "short_description": "Слушайте русское радио Вести ФМ, последние новости о России",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/60bb8d2422b6a2cc35cb31f5",
            "rating": "5,00",
            "category": "Новости и журналы",
            "type": "application",
            "size": 6462120,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "529",
            "did": "627b84194891a5fdaa00ee61",
            "dtitle": "НашаСтанция",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 16,
              "version_name": "1.5",
              "create_at": "2022-05-11T10:00:08.042Z",
              "release_notes": "Тёмная тема, экономия трафика 32 кбит/с",
              "install_path": "https://cdnb.nashstore.ru/store/install/627b89284891a5fdaa00efa4"
            }
          },
          {
            "id": "628286994891a56964639dfd",
            "app_id": "com.kp",
            "title": "KP.Ru - главные новости страны ",
            "short_description": "Новости. Газета. Сайт. Радио",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/f4f537de735180f0b20c3ced",
            "rating": "5,00",
            "category": "Новости и журналы",
            "type": "application",
            "size": 56997341,
            "r_count": "",
            "ar": "18+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "313",
            "did": "628208eb4891a568e11a3893",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 102,
              "version_name": "1.74",
              "create_at": "2022-05-17T09:31:59.82Z",
              "release_notes": "Приложение \"Комсомольская правда\" теперь и в NashStore!",
              "install_path": "https://cdnb.nashstore.ru/store/install/62836b8f4891a5de4cd6d66a"
            }
          },
          {
            "id": "627d03024891a5fdaa011a8e",
            "app_id": "com.vgtrk.smotrim",
            "title": "СМОТРИМ. Россия, ТВ и радио",
            "short_description": "Новости, ток-шоу, фильмы, мультфильмы, подкасты - все в одном приложении!",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/7a07c4b7bce8e4ce9c511a26",
            "rating": "4,71",
            "category": "Развлечения",
            "type": "application",
            "size": 45432234,
            "r_count": "",
            "ar": "18+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "27.9тыс.",
            "did": "627d02dc4891a5fdaa011a8a",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 80409,
              "version_name": "8.4",
              "create_at": "2022-05-12T14:05:00.504Z",
              "release_notes": "Внесли некоторые улучшения и поработали над ошибками, чтобы вам было удобнее пользоваться приложением.",
              "install_path": "https://cdnb.nashstore.ru/store/install/627d140c4891a5fdaa011c99"
            }
          }
        ]
      },
      {
        "id": "6281b2d34891a55c611ecb00",
        "title": "Сервисы для общения",
        "position": "2",
        "type": "promo",
        "description": "Знакомства, мессенджеры, чаты и соцсети",
        "icon": "https://cdnb.nashstore.ru/api/v1/media/68fe59de3e5ab6ec66880ae3",
        "cover": "https://cdnb.nashstore.ru/api/v1/media/97b50cdb11219aa8c71f6e31",
        "apps": [
          {
            "id": "6278f3bf4891a52a3548a727",
            "app_id": "dev.lzrv.colibri",
            "title": "Colibri X — Telegram unofficial",
            "short_description": "Приложение для обмена сообщениями, ориентированное на скорость и безопасность.",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/197dc074647282bb6c86fe3e",
            "rating": "5,00",
            "category": "Социальные",
            "type": "application",
            "size": 64609229,
            "r_count": "",
            "ar": "16+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "138",
            "did": "6278f37d4891a52a3548a6e6",
            "dtitle": "Alexander Lazarev",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 32,
              "version_code": 26400,
              "version_name": "8.7.4",
              "create_at": "2022-05-14T11:34:04.971Z",
              "release_notes": "• Пользовательские звуки уведомлений.\n• Установка любых коротких аудиофайлов в качестве звуков для оповещений.\n• Отключение уведомлений на произвольный период.\n• Беззвучные уведомления.\n• Новое меню автоудаления и гибкие настройки таймера для очистки переписки.\n• Новый дизайн режима «Картинка-в-картинке».\n• Пометки о том, какие из пересланных сообщений являются ответами.\n• Новые сверхмощные боты.",
              "install_path": "https://cdnb.nashstore.ru/store/install/627f93ac4891a527a6f0054f"
            }
          },
          {
            "id": "6278f9f24891a52a3548aba1",
            "app_id": "ru.mobstudio.andgalaxy",
            "title": "Чат знакомств Galaxy",
            "short_description": "Без подписок и номера телефона при регистрации",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/ced8e42b71072867cb2c1110",
            "rating": "5,00",
            "category": "Знакомства",
            "type": "application",
            "size": 7511229,
            "r_count": "",
            "ar": "18+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "1.3тыс.",
            "did": "6278f9db4891a52a3548ab91",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 32,
              "version_code": 9051700,
              "version_name": "9.5.17",
              "create_at": "2022-05-09T11:32:07.338Z",
              "release_notes": "Свежая версия приложения ",
              "install_path": "https://cdnb.nashstore.ru/store/install/6278fbb74891a52a3548ad27"
            }
          },
          {
            "id": "627b6bd64891a5fdaa00e85e",
            "app_id": "app.swiper.mobile",
            "title": "Swiper - лента, чаты",
            "short_description": "Безопасное и удобное общение",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/4d422c5a3096de27f19b7c50",
            "rating": "4,80",
            "category": "Социальные",
            "type": "application",
            "size": 176315706,
            "r_count": "",
            "ar": "12+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "109",
            "did": "627b6baf4891a5fdaa00e852",
            "dtitle": "",
            "release": {
              "sdk_min": 24,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 14,
              "version_name": "1.0.13",
              "create_at": "2022-05-17T20:22:42.391Z",
              "release_notes": "Исправлены ошибки при удалении постов в профиле, оптимизирована работа предварительного редактора публикаций!",
              "install_path": "https://cdnb.nashstore.ru/store/install/628404124891a536bcab8f31"
            }
          },
          {
            "id": "627f88ae4891a527a6f00465",
            "app_id": "app.datebox.dalla",
            "title": "Datebox: знакомства и свидания",
            "short_description": "Выбери идею для свидания, реши кто будет твоей парой и знакомься",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/c2ddf8d24481296dd1c50aa3",
            "rating": "5,00",
            "category": "Знакомства",
            "type": "application",
            "size": 38959045,
            "r_count": "",
            "ar": "18+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "122",
            "did": "627f88584891a527a6f0045c",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 34,
              "version_name": "1.3.0",
              "create_at": "2022-05-17T08:08:58.774Z",
              "release_notes": "Исправления мелких ошибок\nМожно получить монетки бесплатно!",
              "install_path": "https://cdnb.nashstore.ru/store/install/6283581a4891a5438b37b66c"
            }
          }
        ]
      },
      {
        "id": "6281ae284891a55c611ecafa",
        "title": "Банки",
        "position": "2",
        "type": "promo",
        "description": "Финансовые институты, попавшие под санкции, возвращаются",
        "icon": "https://cdnb.nashstore.ru/api/v1/media/d02da584867f000196ec4dc2",
        "cover": "https://cdnb.nashstore.ru/api/v1/media/624883ed9f402f1a772e1472",
        "apps": [
          {
            "id": "62833ba54891a5438b35d44e",
            "app_id": "com.russian.banks",
            "title": "Банки России: сравни все банки",
            "short_description": "Все Банки России. Сравни условия по кредитам, вкладам, ипотеке",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/76b3a38e2ce4a38697a9b6f5",
            "rating": "4,00",
            "category": "Банки",
            "type": "application",
            "size": 25209550,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "108",
            "did": "627ce5814891a5fdaa0115e3",
            "dtitle": "Opendata.mobi",
            "release": {
              "sdk_min": 19,
              "sdk_max": 0,
              "sdk_version": 31,
              "version_code": 9,
              "version_name": "2.0.2",
              "create_at": "2022-05-17T06:09:41.86Z",
              "release_notes": "Все банки России: кредиты, ипотека, вклады, кредитные карты",
              "install_path": "https://cdnb.nashstore.ru/store/install/62833c254891a5438b35d95f"
            }
          },
          {
            "id": "627b72384891a5fdaa00ea2f",
            "app_id": "ru.alfabank.mobile.android",
            "title": "Альфа-Банк",
            "short_description": "Мобильное приложение Альфа-Банка",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/3748de58743e5e2896ebf322",
            "rating": "4,84",
            "category": "Банки",
            "type": "application",
            "size": 143870795,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "49.8тыс.",
            "did": "627b71f94891a5fdaa00ea1f",
            "dtitle": "Альфа-Банк",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 2036115116,
              "version_name": "11.51.16",
              "create_at": "2022-05-11T12:36:33.855Z",
              "release_notes": "В этом обновлении, через раздел Справки и выписки в профиле или витрине, можно заказать справку для госслужащих за отчетный период 2021 года. Справка формируется онлайн — показывает информацию о доходах, расходах, имуществе и обязательствах. В приложении Альфа-Банка справка приходит моментально. Также в приложении появилось автоматическое открытие накопительного счета при заказе и выдаче дебетовой карты.",
              "install_path": "https://cdnb.nashstore.ru/store/install/627badd14891a5fdaa00f7f0"
            }
          },
          {
            "id": "627cd7524891a5fdaa01146a",
            "app_id": "ru.vtb24.mobilebanking.android",
            "title": "ВТБ Онлайн",
            "short_description": "Мобильное приложение ВТБ Онлайн — это полноценный банк в вашем смартфоне!",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/4cf82e363c510c935a9211c7",
            "rating": "4,89",
            "category": "Банки",
            "type": "application",
            "size": 405385212,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "62.7тыс.",
            "did": "627cd62e4891a5fdaa01144d",
            "dtitle": "VTB Bank, PJSC",
            "release": {
              "sdk_min": 23,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 2090140450,
              "version_name": "16.10.0.0",
              "create_at": "2022-05-19T14:01:16.776Z",
              "release_notes": "Запустили сервис проверки ссылок на фишинг — он поможет защититься от ссылок на мошеннические интернет-ресурсы, например, это могут быть копии сайтов известных компаний. Чтобы проверить ссылку, перейдите в раздел «Услуги» > «Проверка ссылок». \n\nЕще добавили несколько улучшений в чат — там появилась возможность отправлять не только фотографии, но и документы. Кстати, теперь вы можете отправить сразу несколько файлов за один раз.\n\nКоманда ВТБ Онлайн",
              "install_path": "https://cdnb.nashstore.ru/store/install/62864dac0a39b277f96748e2"
            }
          },
          {
            "id": "627e12e84891a527a6efeaa9",
            "app_id": "logo.com.mbanking",
            "title": "ПСБ",
            "short_description": "Мобильный. Удобный. Сделан с любовью",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/0a67ecf31d6a61ebfe310702",
            "rating": "4,86",
            "category": "Банки",
            "type": "application",
            "size": 99982046,
            "r_count": "",
            "ar": "12+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "11.6тыс.",
            "did": "627e0c964891a527a6efe9a9",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 338,
              "version_name": "3.53.3",
              "create_at": "2022-05-18T03:56:35.278Z",
              "release_notes": "С каждым обновлением стараемся делать приложение удобнее. \n\nЧто нового в этой версии:\n\n1. Владельцы Android могут привязать свои карты Мир к сервису «Mir Pay» в один клик.\n2. Теперь можно легко узнать реквизиты любой своей карты, а не только виртуальной.\n3. Страховые полисы «Автопомощь» отображаются сразу на главном экране мобильного банка.\n\nДайте знать, насколько удобно пользоваться новым функционалом: оставляйте отзывы и комментарии.",
              "install_path": "https://cdnb.nashstore.ru/store/install/62846e730a39b254006f35a1"
            }
          },
          {
            "id": "627bbf134891a5fdaa00fb93",
            "app_id": "ru.sovcomcard.halva.v1",
            "title": "Халва - Совкомбанк",
            "short_description": "Приложение «Халва – Совкомбанк» — это банковский офис на экране смартфона!",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/d7a96b646e3d0bd83e9dd58a",
            "rating": "4,76",
            "category": "Банки",
            "type": "application",
            "size": 107146617,
            "r_count": "",
            "ar": "0+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "20.9тыс.",
            "did": "627bbe634891a5fdaa00fb76",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 110145600,
              "version_name": "6.6.2",
              "create_at": "2022-05-11T14:33:55.337Z",
              "release_notes": "Приложение «Халва – Совкомбанк» — это банковский офис на экране смартфона!",
              "install_path": "https://cdnb.nashstore.ru/store/install/627bc9534891a5fdaa00fd33"
            }
          },
          {
            "id": "627b6b214891a5fdaa00e823",
            "app_id": "ru.minbank.android",
            "title": "МИнБ",
            "short_description": "Мобильный банк в вашем телефоне!",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/83266d58b9586b89187dea81",
            "rating": "4,50",
            "category": "Банки",
            "type": "application",
            "size": 35770061,
            "r_count": "",
            "ar": "3+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "906",
            "did": "627b6afb4891a5fdaa00e818",
            "dtitle": "",
            "release": {
              "sdk_min": 22,
              "sdk_max": 0,
              "sdk_version": 29,
              "version_code": 20201445,
              "version_name": "4.4.19.6",
              "create_at": "2022-05-11T08:32:37.985Z",
              "release_notes": "- Переход с ПАО на АО;",
              "install_path": "https://cdnb.nashstore.ru/store/install/627b74a54891a5fdaa00eae0"
            }
          },
          {
            "id": "627b60f94891a5fdaa00e4be",
            "app_id": "com.cetelem.cetelem_android",
            "title": "Сетелем - Мой Банк",
            "short_description": "Бесплатный сервис дистанционного обслуживания в формате мобильного приложения. ",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/135ba8f9da812e35cec3ac65",
            "rating": "4,62",
            "category": "Банки",
            "type": "application",
            "size": 37655491,
            "r_count": "",
            "ar": "12+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "1.3тыс.",
            "did": "627b60cd4891a5fdaa00e4ac",
            "dtitle": "Сетелем Банк",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 49,
              "version_name": "2.3.22",
              "create_at": "2022-05-11T08:44:06.111Z",
              "release_notes": "В настоящее время мобильное приложение «Мой банк» недоступно для скачивания в App Store и Google play, но у нас теперь есть NashStore. \nЭто последняя опубликованная версия приложения на сайте Сетелем. \nБлагодарим наших пользователей за отзывы. Скоро будут новые выпуски. ",
              "install_path": "https://cdnb.nashstore.ru/store/install/627b77564891a5fdaa00eb70"
            }
          },
          {
            "id": "627b413c4891a5fdaa00dc1c",
            "app_id": "infinit.vtb",
            "title": "VTB KZ ONLINE",
            "short_description": "Мобильный банкинг",
            "icon": "https://cdnb.nashstore.ru/api/v1/media/53e66adacaa17781de8a8fba",
            "rating": "5,00",
            "category": "Банки",
            "type": "application",
            "size": 30209466,
            "r_count": "",
            "ar": "16+",
            "ard": "",
            "arl": "https://store.nashstore.ru/rules/age_restrictions",
            "installs": "334",
            "did": "627b40ce4891a5fdaa00dc0b",
            "dtitle": "",
            "release": {
              "sdk_min": 21,
              "sdk_max": 0,
              "sdk_version": 30,
              "version_code": 53,
              "version_name": "2.0.3",
              "create_at": "2022-05-11T06:31:27.106Z",
              "release_notes": "Мобильный банкинг для физических лиц",
              "install_path": "https://cdnb.nashstore.ru/store/install/627b583f4891a5fdaa00e23d"
            }
          }
        ]
      }
    ]
  },
  "page": 0,
  "positions": [
    "1",
    "2"
  ],
  "status": "success",
  "total": 4
}

```

</details>

## Icons and Screenshots

URL: "https://icon(screenshot)_url/[original, small]

## Unknown

### Update + Account stuff?

METHOD: POST

URL: "https://store.nashstore.ru/api/mobile/v1/profile/mobile"

REQUEST:

``` json 
    {
        "apps": {
            "org.swiftapps.swiftbackup": {
            "appName": "Swift Backup",
            "versionName": "4.1.0",
            "firstInstallTime": 1653229416920,
            "lastUpdateTime": 1653229416920,
            "versionCode": 545,
            "packageName": "org.swiftapps.swiftbackup"
            },
            "wangdaye.com.geometricweather": {
            "appName": "Geometric Weather",
            "versionName": "3.011_gplay",
            "firstInstallTime": 1653241056237,
            "lastUpdateTime": 1653241056237,
            "versionCode": 30011,
            "packageName": "wangdaye.com.geometricweather"
            },
            (SENT ALL USER APPS INSTALLED ON DEVIECE)
        }
    }

```

Responce:

``` json

{
    "profile": {
        "email": "test.test10003@yandex.ru",
        "first_name": "test",
        "installed_apps": [],
        "last_name": "test",
        "phone": "+79956909669",
        "third_name": ""
    },
    "session": {
        "created_at": "2022-05-22T19:01:17.907Z"
    },
    "status": "success"
} 

```
