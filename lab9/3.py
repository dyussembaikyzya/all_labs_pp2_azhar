import pygame 
 
 
WIDTH, HEIGHT = 1200, 800  # Определяет ширину и высоту игрового окна.
FPS = 90  # Частота обновления экрана
draw = False   # Указывает, рисуем ли на экране           
radius = 2    # Радиус кисти
color = 'blue'  # Цвет кисти
mode = 'pen'    # Режим рисования (по умолчанию ручка)
 
pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Создаем окно с указанными размерами
pygame.display.set_caption('Paint')  # Название окна
clock = pygame.time.Clock()  # Для управления временем
screen.fill(pygame.Color('white'))  # Заполняем экран белым цветом.
font = pygame.font.SysFont('None', 60)  # Создаем шрифт для отображения текста
 
 
def drawLine(screen, start, end, width, color): 
    # Извлекаем координаты начальной и конечной точек
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    
    # Вычисляем абсолютные разницы по осям x и y
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    
    # Коэффициенты для уравнения линии Ax + By + C = 0
    A = y2 - y1  # По вертикали
    B = x1 - x2  # По горизонтали
    C = x2 * y1 - x1 * y2 
    
    # Если линия более горизонтальная, чем вертикальная
    if dx > dy: 
        # Убедитесь, что x1 слева от x2
        if x1 > x2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        # Итерируем по координатам x
        for x in range(x1, x2): 
            # Вычисляем координату y по уравнению линии
            y = (-C - A * x) / B 
            # Рисуем круг (пиксель) в позиции (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
    # Если линия более вертикальная, чем горизонтальная
    else: 
        # Убедитесь, что y1 ниже y2
        if y1 > y2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        # Итерируем по координатам y
        for y in range(y1, y2): 
            # Вычисляем координату x по уравнению линии
            x = (-C - B * y) / A 
            # Рисуем круг (пиксель) в позиции (x, y)
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

 
 
def drawCircle(screen, start, end, width, color): 
    # Извлекаем координаты начальной и конечной точек
    x1 = start[0]  # Извлекаем координату x начальной точки
    x2 = end[0]  # Извлекаем координату x конечной точки
    y1 = start[1]  # Извлекаем координату y начальной точки
    y2 = end[1]  # Извлекаем координату y конечной точки
    
    # Вычисляем центр окружности
    x = (x1 + x2) / 2  # Вычисляем центр окружности по оси x
    y = (y1 + y2) / 2  # Вычисляем центр окружности по оси y
    
    # Вычисляем радиус окружности
    radius = abs(x1 - x2) / 2  # Радиус окружности
    
    # Рисуем окружность на экране
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)  # Рисуем окружность на экране

 
 
def drawRectangle(screen, start, end, width, color): 
    # Извлекаем координаты начальной и конечной точек
    x1 = start[0]  # Извлекаем координату x начальной точки
    x2 = end[0]  # Извлекаем координату x конечной точки
    y1 = start[1]  # Извлекаем координату y начальной точки
    y2 = end[1]  # Извлекаем координату y конечной точки
    
    # Вычисляем ширину и высоту прямоугольника
    widthr = abs(x1 - x2)  # Вычисляем ширину прямоугольника
    height = abs(y1 - y2)  # Вычисляем высоту прямоугольника
    
    # Рисуем прямоугольник на экране в зависимости от положения начальной и конечной точки
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)  # Рисуем прямоугольник на экране
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)  # Рисуем прямоугольник на экране
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)  # Рисуем прямоугольник на экране
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)  # Рисуем прямоугольник на экране

     
 
 
def drawSquare(screen, start, end, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    mn = min(abs(x2 - x1), abs(y2 - y1)) 
 
 
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn)) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn)) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn)) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn)) 
 
def drawRightTriangle(screen, start, end, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
     
    if x2 > x1 and y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
 
 
def drawEquilateralTriangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
 
    width_b = abs(x2 - x1) 
    height = (3**0.5) * width_b / 2 
 
    if y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width) 
    else: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height))) 
     
 
def drawRhombus(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width) 
 
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()  # Выход из программы, если окно закрыто
         
        # Обработка событий клавиш
        if event.type == pygame.KEYDOWN: 
            # Изменение режима в зависимости от нажатой клавиши
            if event.key == pygame.K_r: 
                mode = 'rectangle'  # Устанавливаем режим рисования прямоугольников
            if event.key == pygame.K_c: 
                mode = 'circle'  # Устанавливаем режим рисования окружностей
            if event.key == pygame.K_p: 
                mode = 'pen'  # Устанавливаем режим рисования ручкой
            if event.key == pygame.K_e: 
                mode = 'erase'  # Устанавливаем режим стирания
            if event.key == pygame.K_s: 
                mode = 'square'  # Устанавливаем режим рисования квадратов
            if event.key == pygame.K_q: 
                screen.fill(pygame.Color('white'))  # Очищаем экран, заполняя его белым цветом
 
            # Изменение цвета в зависимости от нажатой клавиши
            if event.key == pygame.K_1: 
                color = 'black'  # Устанавливаем цвет в черный
            if event.key == pygame.K_2: 
                color = 'green'  # Устанавливаем цвет в зеленый
            if event.key == pygame.K_3: 
                color = 'red'  # Устанавливаем цвет в красный
            if event.key == pygame.K_4: 
                color = 'blue'  # Устанавливаем цвет в синий
            if event.key == pygame.K_5: 
                color = 'yellow'  # Устанавливаем цвет в желтый
            if event.key == pygame.K_t: 
                mode = 'right_tri'  # Устанавливаем режим рисования прямоугольных треугольников
            if event.key == pygame.K_u: 
                mode = 'eq_tri'  # Устанавливаем режим рисования равносторонних треугольников
            if event.key == pygame.K_h: 
                mode = 'rhombus'  # Устанавливаем режим рисования ромбов
 
      
        if event.type == pygame.MOUSEBUTTONDOWN:  
            draw = True  # Включаем режим рисования
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)  # Рисуем круг (пиксель) если активен режим ручки
            prevPos = event.pos  # Сохраняем текущую позицию как предыдущую

 
        
        if event.type == pygame.MOUSEBUTTONUP:  
        # Когда кнопка мыши отпущена
            if mode == 'rectangle': 
                drawRectangle(screen, prevPos, event.pos, radius, color)  # Рисуем прямоугольник, если активен режим прямоугольника
            elif mode == 'circle': 
                drawCircle(screen, prevPos, event.pos, radius, color)  # Рисуем окружность, если активен режим окружности
            elif mode == 'square': 
                drawSquare(screen, prevPos, event.pos, color)  # Рисуем квадрат, если активен режим квадрата
            elif mode == 'right_tri': 
                drawRightTriangle(screen, prevPos, event.pos, color)  # Рисуем прямоугольный треугольник, если активен режим
            elif mode == 'eq_tri': 
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)  # Рисуем равносторонний треугольник
            elif mode == 'rhombus': 
                drawRhombus(screen, prevPos, event.pos, radius, color)  # Рисуем ромб, если активен режим ромба
            draw = False  # Выключаем режим рисования

 
       
        if event.type == pygame.MOUSEMOTION:  
        # Когда мышь движется
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color)  # Если рисование включено и активен режим ручки, рисуем линию между предыдущей и текущей позицией
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white')  # Если рисование включено и активен режим стирания, рисуем белую линию (стираем)
            lastPos = event.pos  # Обновляем последнюю позицию

    # Рисуем прямоугольник для отображения информации о радиусе
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))  # Рисуем белый прямоугольник для отображения радиуса
    renderRadius = font.render(str(radius), True, pygame.Color(color))  # Отображаем текст с текущим радиусом
    screen.blit(renderRadius, (5, 5))  # Выводим текст на экран в указанной позиции
 
    pygame.display.flip()  # Обновляем отображение
    clock.tick(FPS)  # Управляем частотой кадров
