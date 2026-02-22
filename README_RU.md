# OpenCore Legacy Patcher 3.1.6 - Набор заплаток для Tahoe (YBronst)

Этот проект продолжает набор заплаток для Tahoe, основанный на коммите `lzhoang2801` от 24 декабря 2025 года, и адаптирует его для новой среды macOS Tahoe.

## Важное примечание о совместимости

Этот репозиторий поддерживает:
* **macOS Tahoe 26.0 – 26.3**
* **Поддержка macOS Tahoe 26.4 и новее** будет реализована как можно скорее

> [!IMPORTANT]
> Начиная с macOS 26.4 beta 1, Apple внесла значительные изменения в процесс обновления системы. Предыдущий процесс обновления Tahoe не может функционировать без модификаций в этих версиях.

### В частности:
* Предыдущая обработка **образов заплаток на базе HFS** больше не принимается операционной системой.
* Монтирование образов через [`hdiutil`](https://github.com/YBronst/tccplus) теперь требует **повышенных привилегий** и не может быть выполнено в контексте обычного пользователя. Из-за этого оригинальный рабочий процесс OCLP 3.0.0 Nightly не может завершить процесс установки корневых заплаток в macOS 26.4 без модификации.

## Ключевые изменения в 3.1.6
Добавлен переключатель в раздел «Корневые заплатки» для включения/выключения заплатки «Modern Audio» для восстановления AppleHDA. Это предотвращает неустранимые паники ядра в macOS Tahoe без установленного KDK.

## Ключевые изменения в 3.1.5
* Сохранена **обратная совместимость** с macOS Tahoe 26.0–26.3.
* **Обработка образов заплаток** была мигрирована на APFS для совместимости с macOS 26.4.
* Добавлена **логика привилегированного монтирования**, которая необходима для доступа к внутренним образам заплаток и системным ресурсам.
* **AMFIPass** нельзя использовать с OCLP 3.1.5 из-за постоянной паники ядра. Вместо этого используйте аргумент загрузки `amfi=0x80` и управление разрешениями приложений на основе [`tccplus`](https://github.com/YBronst/tccplus).

## Modern Audio (AppleHDA)
В macOS 26.4 beta 1 установка заплатки Modern Audio временно **не рекомендуется** до тех пор, пока не станет доступен соответствующий комплект отладки ядра (KDK).

Для систем, требующих полностью функциональную эталонную среду (включая звук) в macOS 26.3 и ранее, я рекомендую сохраненный и рабочий снимок заплаток от 24 декабря, доступный здесь: [`OCLP-lzhoang2801`](https://github.com/kgp-macPro/OCLP-lzhoang2801)

*Примечание: Этот набор заплаток по-прежнему требует аргумента загрузки `amfi=0x80`.*

---
## Благодарности

* [Acidanthera](https://github.com/Acidanthera)
  * OpenCorePkg, а также многие основные кексты и инструменты
* [DhinakG](https://github.com/DhinakG)
  * Основной соавтор
* [Khronokernel](https://github.com/Khronokernel)
  * Основной соавтор
* [Ausdauersportler](https://github.com/Ausdauersportler)
  * Набор заплаток и документация по обновлению Metal GPU в iMac
  * Огромная помощь в отладке и предложения по коду
* [vit9696](https://github.com/vit9696)
  * Бесконечная помощь в поиске и устранении неисправностей, определении исправлений и написании патчей
* [EduCovas](https://github.com/covasedu)
  * [Набор заплаток non-Metal](https://github.com/moraea/non-metal-frameworks) для GPU nVidia Tesla/Fermi/Maxwell/Pascal, AMD TeraScale 1/2 и Intel Core 1-го/2-го поколений
  * [Набор заплаток 3802 Metal](https://github.com/moraea/misc-patches/tree/main/3802-Metal-15) и [MetallibSupportPkg](https://github.com/dortania/MetallibSupportPkg) для GPU nVidia Kepler и Intel Core 3-го/4-го поколений
  * Патчи и прослойки Metal bundle для [nVidia Kepler](https://github.com/moraea/misc-patches/tree/main/Kepler%2013%2B), [AMD GCN 1 - 4](https://github.com/moraea/misc-patches/tree/main/GCN%2013%2B) и [AMD GCN 5 (Vega)](https://github.com/moraea/misc-patches/tree/main/vega%2013%2B)
  * [Патчи смещения IOSurface](https://github.com/moraea/misc-patches/tree/main/Sonoma%2014.4%20IOSurface) для nVidia Kepler, AMD GCN 1 - 5 и Intel Core 3-го - 6-го поколений
  * [Набор заплаток для устаревшего Wi-Fi](https://github.com/moraea/unsupported-wifi-patches) восстанавливает функциональность карт Wi-Fi во всех моделях 2007–2017 годов
  * [Набор заплаток T1](https://github.com/moraea/misc-patches/tree/main/T1-Patch) восстанавливает Touch ID, Apple Pay и другие функции безопасности в моделях 2016–2017 годов
  * Даунгрейд AppleGVA для ускоренного декодирования видео на моделях 2012–2016 годов
  * Даунгрейд OpenCL и OpenGL для AMD GCN
  * [Патч USB 1](https://github.com/moraea/misc-patches/tree/main/IOUSBHostFamily-14.4)
* [ASentientHedgehog](https://github.com/moosethegoose2213)
  * [Набор заплаток non-Metal](https://github.com/moraea/non-metal-frameworks) для GPU nVidia Tesla/Fermi/Maxwell/Pascal, AMD TeraScale 1/2 и Intel Core 1-го/2-го поколений
* [ASentientBot](https://github.com/ASentientBot)
  * [Набор заплаток non-Metal](https://github.com/moraea/non-metal-frameworks) для GPU nVidia Tesla/Fermi/Maxwell/Pascal, AMD TeraScale 1/2 и Intel Core 1-го/2-го поколений
  * [Интерпозер Metal bundle](https://github.com/moraea/misc-patches/tree/main/sequoia%2031001%20interposer) для AMD GCN 1 - 5 и Intel Core 5-го/6-го поколений
  * [dsce](https://github.com/moraea/dsce) и [общий код](https://github.com/moraea/moraea-common), используемый некоторыми другими патчами
* [cdf](https://github.com/cdf)
  * Набор заплаток и документация для Mac Pro на OpenCore
  * [Innie](https://github.com/cdf/Innie) и [NightShiftEnabler](https://github.com/cdf/NightShiftEnabler)
* [Syncretic](https://forums.macrumors.com/members/syncretic.1173816/)
  * [AAAMouSSE](https://forums.macrumors.com/threads/mp3-1-others-sse-4-2-emulation-to-enable-amd-metal-driver.2206682/), [telemetrap](https://forums.macrumors.com/threads/mp3-1-others-sse-4-2-emulation-to-enable-amd-metal-driver.2206682/post-28447707) и [SurPlus](https://github.com/reenigneorcim/SurPlus)
* [dosdude1](https://github.com/dosdude1)
  * Основной автор [оригинального GUI](https://github.com/dortania/OCLP-GUI)
  * Разработка предыдущих патчеров, определение многого из того, что требует исправлений
* [parrotgeek1](https://github.com/parrotgeek1)
  * [Набор заплаток VMM](https://github.com/dortania/OpenCore-Legacy-Patcher/blob/4a8f61a01da72b38a4b2250386cc4b497a31a839/payloads/Config/config.plist#L1222-L1281)
* [BarryKN](https://github.com/BarryKN)
  * Разработка предыдущих патчеров, определение многого из того, что требует исправлений
* [mario_bros_tech](https://github.com/mariobrostech) и остальная часть сообщества Unsupported Mac Discord
  * Катализатор, с которого начался OpenCore Legacy Patcher
* [arter97](https://github.com/arter97/)
  * [SimpleMSR](https://github.com/arter97/SimpleMSR/) для отключения троттлинга прошивки в ноутбуках Nehalem+ без аккумуляторов
* [Mr.Macintosh](https://mrmacintosh.com)
  * Бесконечные часы помощи в архитектуре и устранении неисправностей во многих частях проекта
* [flagers](https://github.com/flagersgit)
  * Помощь в исследовании и разработке веб-драйверов Nvidia
  * [Набор заплаток non-Metal](https://github.com/moraea/non-metal-frameworks) для GPU nVidia Tesla/Fermi/Maxwell/Pascal, AMD TeraScale 1/2 и Intel Core 1-го/2-го поколений
  * [Интерпозер Metal bundle](https://github.com/moraea/misc-patches/tree/main/sequoia%2031001%20interposer) для AMD GCN 1 - 5 и Intel Core 5-го/6-го поколений
  * LegacyRVPL, SnapshotIsKill и т. д. для помощи в быстром тестировании и разработке
* [joevt](https://github.com/joevt)
  * [FixPCIeLinkrate](https://github.com/joevt/joevtApps)
* [Jazzzny](https://github.com/Jazzzny)
  * Исследования и различные вклады в проект
  * Исследование и разработка UEFI Legacy XHCI
  * Исследование и разработка NVIDIA OpenCL
  * Исследование и разработка для `MacBook5,2`
    * LegacyKeyboardInjector
  * Патч для Aquantia Ethernet на системах до Ivy Bridge
  * Патч для Photo Booth (non-Metal) для Monterey+
  * Разработка графического интерфейса и серверной части
    * Интерфейс средства обновления
    * Интерфейс загрузчика macOS
    * Интерфейс загрузчика
    * Проверка USB Top Case
    * Применение корневых заплаток для разработчиков
  * Реализация Vaulting
  * Исследование macOS 15 3802 Helios
  * Исследование UEFI bootx64.efi
  * Исследование сборки universal2
  * Различные вклады в документацию
* Замечательные пользователи, любезно пожертвовавшие оборудование:
  * [JohnD](https://forums.macrumors.com/members/johnd.53633/) - 2013 Mac Pro
  * [SpiGAndromeda](https://github.com/SpiGAndromeda) - AMD Vega 64
  * [turbomacs](https://github.com/turbomacs) - 2014 5k iMac
  * [vinaypundith](https://forums.macrumors.com/members/vinaypundith.1212357/) - MacBook7,1
  * [ThatStella7922](https://github.com/ThatStella7922) - 2017 13" MacBook Pro (A1708)
  * zephar - 2008 Mac Pro
  * jazo97 - 2011 15" MacBook Pro
  * И другие (свяжитесь с нами, если мы кого-то забыли!)
* Сообщества MacRumors и Unsupported Mac
  * Бесконечное тестирование и сообщения об ошибках
* Apple
  * за macOS и многие кексты, фреймворки и другие бинарные файлы, которые мы перенесли в новые ОС

## Отказ от ответственности
Это **не официальный релиз Dortania**, он предназначен для сложных конфигураций Hackintosh.

**Спасибо:**
* Команде Dortania OCLP
* lzhoang2801
* Всем участникам PatcherSupportPkg

**Обсуждение в сообществе:** [Тема на InsanelyMac](https://www.insanelymac.com/forum/topic/362042-experimental-fork-of-oclp-300-nightly-–-wi-fi-airdropairplay-and-applehda-fully-working-under-tahoe/)
