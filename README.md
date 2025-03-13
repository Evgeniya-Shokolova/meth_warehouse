Рулон: id, длина, вес, дата добавления, дата удаления.
Обязательные пункты:
1. RESTFull API:
a. добавление нового рулона на склад. Длина и вес — обязательные
параметры. В случае успеха возвращает добавленный рулон;
b. удаление рулона с указанным id со склада. В случае успеха возвращает
удалённый рулон;
c. получение списка рулонов со склада. Рассмотреть возможность
фильтрации по одному из диапазонов единовременно (id/веса/длины/даты
добавления/даты удаления со склада);
d. получение статистики по рулонам за определённый период:
 количество добавленных рулонов;
 количество удалённых рулонов;
 средняя длина, вес рулонов, находившихся на складе в этот период;
 максимальная и минимальная длина и вес рулонов, находившихся на
складе в этот период;
 суммарный вес рулонов на складе за период;
 максимальный и минимальный промежуток между добавлением и
удалением рулона.