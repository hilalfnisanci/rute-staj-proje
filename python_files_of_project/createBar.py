from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CreateBar():

    def paintEvent(self, painter, barName, page, progressValue):
        
        pen = QPen()

        # paintEvent start for kV bar 
        if barName == "kV":
            
            if page == "du1":
                # kullanılacak sayısal değerler verilir
                text_x = 105    # kV barında değerlerin yazılmaya başlanacağı x değeri  
                text_y = 135    # kV barında değerlerin yazılmaya başlanacağı y değeri
                scaleCount = 4  # kV barında 4 değer bulunuyor
                increment = 5   # kV barındaki artış değeri
                rect_x = 140    # dörtgenin başlangıç x değeri
                rect_y = 130    # dörtgenin başlangıç y değeri
                rect_w = 40     # dörtgenin width değeri
                rect_h = 220    # dörtgenin height değeri  

            if page == "du2":
                # kullanılacak sayısal değerler verilir
                text_x = 450    # kV barında değerlerin yazılmaya başlanacağı x değeri  
                text_y = 135    # kV barında değerlerin yazılmaya başlanacağı y değeri  
                scaleCount = 4  # kV barında 4 değer bulunuyor
                increment = 5   # kV barındaki artış değeri
                rect_x = 488    # dörtgenin başlangıç x değeri   
                rect_y = 130    # dörtgenin başlangıç y değeri   
                rect_w = 40     # dörtgenin width değeri 
                rect_h = 220    # dörtgenin height değeri       

            # yazı için kalem özellikleri ayarlanır
            pen.setWidth(60)
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            # barın adı yazılır
            painter.drawText(rect_x+18, rect_y-5, barName)
                
            # bardaki ölçek sayıları yazılır
            for i in range(scaleCount):
                if i == 3:
                    start_y = (i - 1) * 80 + 45 + text_y
                    painter.drawText(text_x, start_y + 10, str(0))
                else:
                    start_y = i * 80 + text_y
                    painter.drawText(text_x, start_y + 10, str(30 - i * increment))

            # geometrik çizimler için kalem ayarlanır
            painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
                
            # bar çizimi yapılır
            painter.drawRect(rect_x, rect_y, rect_w, rect_h)

            # bardaki büyük ölçek çizgileri çizilir
            for i in range(scaleCount):
                if i == 0:
                    scale_y = rect_y + 10
                if i == 3:
                    scale_y = 350
                else:
                    scale_y = i * 80 + (rect_y + 10)
                painter.drawLine(rect_x-18, scale_y, rect_x, scale_y)
                
            # bardaki küçük ölçek çizgileri çizilir
            for i in range((scaleCount - 1) * 5):
                scale_y = i * 16 + (rect_y + 10)
                if scale_y >= 310:
                    break
                painter.drawLine(rect_x-6, scale_y, rect_x, scale_y)

            # progress kısmı çizilir
            if progressValue >=0 and progressValue <=30:
                if progressValue <= 20:
                    progressValue = progressValue * 2 + 9
                else:
                    progressValue = (progressValue - 20) * 16 + 50
                
                rect = QRectF(rect_x + 1, rect_y+rect_h - progressValue, rect_w-2, progressValue)
                painter.fillRect(rect, QBrush(Qt.blue))
        # paintevent end for kV bar

        # paintEvent start for A bar
        if barName == "A":
            
            if page == "du1":
                text_x = 190
                text_y = 170
                rect_x = 230
                rect_y = 130
                rect_w = 30
                rect_h = 220
                scaleCount = 5
                increment = 200
                spaceVal = (int) (rect_h / scaleCount)
                scale_y = rect_y + spaceVal
            if page == "du2":
                text_x = 540
                text_y = 125
                rect_x = 580
                rect_y = 130
                rect_w = 30
                rect_h = 208
                scaleCount = 9
                increment = 100
                spaceVal = (int)(rect_h / (scaleCount - 1))
                scale_y = rect_y
            
            pen.setWidth(60)
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            # barın adı yazılır
            painter.drawText(rect_x + 13, rect_y-5, barName)

            # ölçekteki sayısal değerler yazılır
            for i in range(scaleCount):
                if i == scaleCount - 1:
                    start_y = rect_y + rect_h
                    painter.drawText(text_x, start_y + 5, str(0))
                else:
                    start_y = i * spaceVal + text_y
                    painter.drawText(text_x, start_y + 10, str(800 - i * increment))
            
            # geometrik çizimler için kalem ayarlanır
            painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
                
            # bar çizimi yapılır
            painter.drawRect(rect_x, rect_y, rect_w, rect_h)

            # bardaki büyük ölçek çizgileri çizilir
            for i in range(scaleCount):
                if i == 0:
                    painter.drawLine(rect_x-15,scale_y, rect_x, scale_y)
                else:
                    scale_y += spaceVal
                    painter.drawLine(rect_x-15, scale_y, rect_x, scale_y)

            # bardaki küçük ölçek çizgileri çizilir
            for i in range(scaleCount):
                if page == "du2" and i == scaleCount-1:
                    break
                if i == 0:
                    scale_y = rect_y + (int)(spaceVal / 2)
                    painter.drawLine(rect_x-8, scale_y, rect_x, scale_y)
                if i > 0:
                    scale_y += spaceVal
                    painter.drawLine(rect_x-8, scale_y, rect_x, scale_y)
            
            if progressValue >=0 and progressValue <= 800:
                progressValue = (float)(progressValue / increment) * spaceVal
                rect = QRectF(rect_x + 1, rect_y+rect_h - progressValue, rect_w - 1, progressValue - 1)
                painter.fillRect(rect, QBrush(Qt.red))
        # paintEvent end for A bar

        # paintEvent start for kN bar
        if barName == "kN":
            scaleCountLeft = 7
            scaleCountRight = 11
            incrementLeft = 50
            incrementRight = 10
            rect_h = 210
            rect_w = 40
            rect_x = 350
            rect_y = 130
            text_x = 310 # text değerleri sol taraf için yazılmıştır, 
            text_y = 135 # sağ taraf bu değerlerden elde edilecektir
            spaceValLeft = (int) (rect_h / (scaleCountLeft))
            spaceValRight = (int) (rect_h / (scaleCountRight - 1))
            # yazı için kalem özellikleri ayarlanır
            pen.setWidth(60)
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            # barın adı yazılır
            painter.drawText(rect_x - 20, rect_y - 5, barName)

            # bardaki sayı değerleri yazılır
            
            # barın sol tarafı için
            for i in range(scaleCountLeft):
                if i == scaleCountLeft - 1:
                    painter.drawText(text_x, rect_y + rect_h, str(0))
                painter.drawText(text_x, rect_y + i*spaceValLeft + spaceValLeft , str(300 - i*incrementLeft))
            
            # barın sağ tarafı için
            for i in range(scaleCountRight):
                painter.drawText(text_x + 105, rect_y + i*spaceValRight , str(100 - i*incrementRight))

            # geometrik çizimler için kalem ayarlanır
            painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
                
            # bar çizimi yapılır
            painter.drawRect(rect_x, rect_y, rect_w, rect_h)

            # barın sol tarafındaki büyük ölçek çizgileri çizilir
            for i in range(scaleCountLeft):
                if i == scaleCountLeft - 1:
                    painter.drawLine(rect_x - 15, rect_y + rect_h, rect_x, rect_y + rect_h)
                if i != 0:
                    painter.drawLine(rect_x-15, rect_y + i*spaceValLeft, rect_x, rect_y + i*spaceValLeft)

            # barın sağ tarafındaki büyük ölçek çizgileri çizilir
            for i in range(scaleCountRight):
                painter.drawLine(rect_x + rect_w, rect_y + i*spaceValRight, rect_x + rect_w + 15, rect_y + i*spaceValRight)

            # barın sol tarafındaki küçük ölçek çizgileri çizilir
            for i in range(scaleCountLeft):
                if i == 0:
                    scale_y = rect_y + (int)(spaceValRight / 2 + 4)
                    painter.drawLine(rect_x-8, scale_y, rect_x, scale_y)
                else:
                    scale_y += spaceValLeft
                    painter.drawLine(rect_x-8, scale_y, rect_x, scale_y)
            
            if progressValue >= 0 and progressValue <= 300:
                progressValue = (float)(progressValue / incrementLeft) * spaceValLeft
                rect = QRectF(rect_x + 1, rect_y + rect_h - progressValue, rect_w - 1, progressValue )
                painter.fillRect(rect, QBrush(Qt.green))
        # paintEvent end for kN bar

        # paintEvent start for kN/FM bar
        if barName == "kN/FM":
            text_x = 620
            text_y = 125
            rect_x = 650
            rect_y = 130
            rect_w = 30
            rect_h = 220
            scaleCount = 11
            increment = 40
            spaceVal = (int) (rect_h / (scaleCount - 1))
            scale_y = rect_y
        
            pen.setWidth(60)
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            # barın adı yazılır
            painter.drawText(rect_x, rect_y - 10, barName)

            # ölçekteki sayısal değerler yazılır
            for i in range(scaleCount):
                if i == scaleCount - 1:
                    start_y = rect_y + rect_h
                    painter.drawText(text_x, start_y + 5, str(0))
                else:
                    start_y = i * spaceVal + text_y
                    painter.drawText(text_x, start_y + 10, str(400 - i * increment))
            
            # geometrik çizimler için kalem ayarlanır
            painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))

            # bar çizimi yapılır
            painter.drawRect(rect_x, rect_y, rect_w, rect_h)

            # bardaki büyük ölçek değerleri çizilir
            for i in range(scaleCount):
                if i == 0:
                    painter.drawLine(rect_x - 8, scale_y, rect_x, scale_y)
                else:
                    scale_y += spaceVal
                    painter.drawLine(rect_x - 8, scale_y, rect_x, scale_y)

            # progress kısmı

            if progressValue >= 0 and progressValue <= 400:
                progressValue = (float) (progressValue / increment) * spaceVal
                rect = QRectF(rect_x + 1, rect_y + rect_h - progressValue, rect_w - 1, progressValue)
                painter.fillRect(rect, QBrush(Qt.blue))
        # paintEvent end for kN/FM bar        

        # paintEvent start for BatV bar
        if barName == "BatV":
            text_x = 700
            text_y = 125
            rect_x = 740
            rect_y = 130
            rect_w = 30
            rect_h = 204
            scaleCount = 7
            increment = 20
            spaceVal = (int) (rect_h / (scaleCount - 1))
            scale_y = rect_y

            pen.setWidth(60)
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            # barın adı yazılır
            painter.drawText(rect_x, rect_y - 10, barName)

            # değerin gösterildiği kutuya değer yazılır
            pen.setColor(QColor("blue"))
            painter.setPen(pen)
            painter.drawText(rect_x + 5, rect_y + rect_h + 18, str(int(progressValue)))


            # değiştirilen kalem rengi düzeltilir
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            # ölçekteki sayısal değerler yazılır
            for i in range(scaleCount):
                if i == scaleCount - 1:
                    start_y = rect_h + rect_y
                    painter.drawText(text_x, start_y, str(0))
                else:
                    start_y = i * spaceVal + text_y
                    painter.drawText(text_x, start_y + 10, str(120 - i * increment))
            
            # geometrik çizimler için kalem ayarlanır
            painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
                
            # bar çizimi yapılır
            painter.drawRect(rect_x, rect_y, rect_w, rect_h)

            # bardaki büyük ölçek çizgileri çizilir
            for i in range(scaleCount):
                if i == 0:
                    painter.drawLine(rect_x - 15, scale_y, rect_x, scale_y)
                else:
                    scale_y += spaceVal
                    painter.drawLine(rect_x - 15, scale_y, rect_x, scale_y)
            
            # bardaki ara ölçek çizgileri çizilir
            for i in range(scaleCount):
                if i == scaleCount - 1:
                    break
                if i == 0:
                    scale_y = rect_y + (int) (spaceVal / 2)
                    painter.drawLine(rect_x - 15, scale_y, rect_x, scale_y)
                if i > 0:
                    scale_y += spaceVal
                    painter.drawLine(rect_x - 15, scale_y, rect_x, scale_y)

            # değerin gösterildiği küçük kutu çizilir
            painter.drawRect(rect_x, rect_y + rect_h + 5, rect_w, 20)

            # progress kısmı
            if progressValue >= 0 and progressValue <= 120:
                progressValue = (float)(progressValue / increment) * spaceVal
                rect = QRectF(rect_x + 1, rect_y + rect_h - progressValue, rect_w - 1, progressValue)
                painter.fillRect(rect, QBrush(Qt.blue))

        if barName == "brakeBar1":
            rect_x = 502
            rect_y = 110
            rect_h = 210
            rect_w = 60
            text_x = 460
            text_y = 105
            incrementLeft = 0.5
            incrementRight = 1

            scaleCountLeft = 8
            scaleCountRight = 12
            spaceValRight = (int) (rect_h / (scaleCountRight - 1))
            spaceValLeft = (int) (rect_h / (scaleCountLeft - 1))
            spaceVal = (int) (rect_h / (scaleCountLeft - 1))

            pen.setWidth(60)
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            # ölçekteki sayısal değerler yazılır
            for i in range(scaleCountLeft):
                if i == scaleCountLeft - 1:
                    start_y = rect_h + rect_y
                    painter.drawText(text_x, start_y, str(0))
                else:
                    start_y = i * spaceVal + text_y
                    painter.drawText(text_x, start_y + 10, str(6.0 - i * incrementLeft))

            # barın sağ tarafı için
            for i in range(scaleCountRight):
                if i == 0:
                    painter.drawText(text_x + 125, rect_y + i*spaceValRight + 3, "FS")
                if i == 1:
                    painter.drawText(text_x + 125, rect_y + i*spaceValRight + 3, "RP")
                if i == 2:
                    painter.drawText(text_x + 125, rect_y + i*spaceValRight + 3, "1A")
                if i == 3:
                    painter.drawText(text_x + 125, rect_y + i*spaceValRight + 3, "1B")
                if i >= 4 and i <scaleCountRight - 2:
                    painter.drawText(text_x + 125, rect_y + i*spaceValRight + 3, str(-2 + i*incrementRight))
                if i == scaleCountRight - 2:
                    painter.drawText(text_x + 125, rect_y + i*spaceValRight + 3, "MB")
                if i == scaleCountRight - 1:
                    painter.drawText(text_x + 125, rect_y + i*spaceValRight + 3, "EB")

            # geometrik çizimler için kalem ayarlanır
            painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
                
            # bar çizimi yapılır
            painter.drawRect(rect_x, rect_y, rect_w, rect_h)

            # barın sağ tarafındaki büyük ölçek çizgileri çizilir
            for i in range(scaleCountRight):
                painter.drawLine(rect_x + rect_w, rect_y + i*spaceValRight, rect_x + rect_w + 15, rect_y + i*spaceValRight)

            # barın sol tarafındaki büyük ölçek çizgileri çizilir
            for i in range(scaleCountLeft):
                if i == scaleCountLeft - 1:
                    painter.drawLine(rect_x - 15, rect_y + rect_h, rect_x, rect_y + rect_h)
                else:
                    painter.drawLine(rect_x-15, rect_y + i*spaceValLeft, rect_x, rect_y + i*spaceValLeft)

            # progress kısmı
            if progressValue >=0 and progressValue <= 3.0:
                progressValue = progressValue * 10.0
                
            elif progressValue > 3.0 and progressValue <= 6.0:
                progressValue = 30.0 + (progressValue - 3)*60.0
            rect = QRectF(rect_x + 1, rect_y + rect_h - progressValue, rect_w - 1, progressValue)
            painter.fillRect(rect, QBrush(Qt.yellow))
                
        if barName == "brakeBar2":
            rect_x = 630
            rect_y = 140
            rect_h = 180
            rect_w = 60 
            text_x = 610
            text_y = 135
            scaleCount = 7
            spaceVal = (int) (rect_h / (scaleCount - 1))

            pen.setWidth(60)
            pen.setColor(QColor("white"))
            painter.setPen(pen)

            for i in range(scaleCount):
                if i == scaleCount - 1:
                    start_y = rect_h + rect_y
                    painter.drawText(text_x, start_y, str(0))
                else:
                    start_y = i * spaceVal + text_y
                    painter.drawText(text_x, start_y + 10, str(6 - i))
            # geometrik çizimler için kalem ayarlanır
            painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
                
            # bar çizimi yapılır
            painter.drawRect(rect_x, rect_y, rect_w, rect_h)
            painter.drawLine(rect_x + int(rect_w / 2) - 4, rect_y, rect_x + int(rect_w / 2) - 4, rect_y + rect_h)
            painter.drawLine(rect_x + int(rect_w / 2) + 4, rect_y, rect_x + int(rect_w / 2) + 4, rect_y + rect_h)

            # aradaki küçük çizgiler çizilir
            for i in range(1,12):
                painter.drawLine(rect_x + int(rect_w / 2) - 4, rect_y + i* int(rect_h / 12), rect_x + int(rect_w / 2) + 4, rect_y + i* int(rect_h / 12))

            # ölçek çizgileri çizilir
            for i in range(scaleCount):
                # büyük ölçek çizgilerini çizmek için
                painter.drawLine(rect_x - 9, rect_y + i * int(rect_h / (scaleCount-1)), rect_x, rect_y + i * int(rect_h / (scaleCount-1)))
                # küçük ölçek çizgilerini çizmek için
                painter.drawLine(rect_x - 5, rect_y + int(rect_h / 12) + i*int(rect_h / (scaleCount-1)), rect_x, rect_y + int(rect_h / 12) + i*int(rect_h / (scaleCount-1)))
            

            if 0 <= progressValue <=6:
                progressValue = progressValue*30
            
            rect = QRectF(rect_x + 1, rect_y + rect_h - progressValue, int(rect_w / 2) - 5, progressValue)
            painter.fillRect(rect, QBrush(Qt.yellow))

            rect2 = QRectF(rect_x + int(rect_w / 2) + 5, rect_y + rect_h - progressValue, int(rect_w / 2) - 4, progressValue)
            painter.fillRect(rect2, QBrush(Qt.yellow))
