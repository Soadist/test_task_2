# test_task_2

Задача 2</br>
Дан файл, содержащий имена файлов, алгоритм хэширования (один из MD5/SHA1/SHA256) и соответствующие им хэш-суммы, вычисленные по соответствующему алгоритму и указанные в файле через пробел. Напишите программу, читающую данный файл и проверяющую целостность файлов.</br>
Пример</br>
Файл сумм:</br>
`file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906`</br>
`file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e`</br>
`file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e`</br>
`file_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709`</br>
Пример вызова:</br>
<your program> <path to the input file> <path to the directory containing the files to check></br>
Формат вывода: </br>
`file_01.bin OK`</br>
`file_02.bin FAIL`</br>
`file_03.bin NOT FOUND`</br>
`file_04.txt OK`</br>

# Решение</br>

Запуск через python task_2.py <input_file_path> <check_dir_path>

В input_file использование экранирования и кавычек для файлов с пробельными символами не допускается и не требуется.

Для запуска используется python версии не ниже 3.8
