# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgScan.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(228, 134)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.maxIPLayout = QHBoxLayout()
        self.maxIPLayout.setObjectName(u"maxIPLayout")
        self.labMaxIP_1 = QLabel(Dialog)
        self.labMaxIP_1.setObjectName(u"labMaxIP_1")

        self.maxIPLayout.addWidget(self.labMaxIP_1)

        self.spinBox_MaxIP = QSpinBox(Dialog)
        self.spinBox_MaxIP.setObjectName(u"spinBox_MaxIP")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_MaxIP.sizePolicy().hasHeightForWidth())
        self.spinBox_MaxIP.setSizePolicy(sizePolicy)
        self.spinBox_MaxIP.setMinimum(5)
        self.spinBox_MaxIP.setMaximum(200)
        self.spinBox_MaxIP.setValue(15)

        self.maxIPLayout.addWidget(self.spinBox_MaxIP)

        self.labMaxIP_2 = QLabel(Dialog)
        self.labMaxIP_2.setObjectName(u"labMaxIP_2")

        self.maxIPLayout.addWidget(self.labMaxIP_2)


        self.verticalLayout.addLayout(self.maxIPLayout)

        self.threadsLayout = QHBoxLayout()
        self.threadsLayout.setObjectName(u"threadsLayout")
        self.labThreads = QLabel(Dialog)
        self.labThreads.setObjectName(u"labThreads")

        self.threadsLayout.addWidget(self.labThreads)

        self.comboBox_threads = QComboBox(Dialog)
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.addItem("")
        self.comboBox_threads.setObjectName(u"comboBox_threads")
        sizePolicy.setHeightForWidth(self.comboBox_threads.sizePolicy().hasHeightForWidth())
        self.comboBox_threads.setSizePolicy(sizePolicy)

        self.threadsLayout.addWidget(self.comboBox_threads)


        self.verticalLayout.addLayout(self.threadsLayout)

        self.chkBoxLayout = QHBoxLayout()
        self.chkBoxLayout.setObjectName(u"chkBoxLayout")
        self.chkBox_optimize = QCheckBox(Dialog)
        self.chkBox_optimize.setObjectName(u"chkBox_optimize")
        self.chkBox_optimize.setChecked(True)

        self.chkBoxLayout.addWidget(self.chkBox_optimize)

        self.chkBox_autoTest = QCheckBox(Dialog)
        self.chkBox_autoTest.setObjectName(u"chkBox_autoTest")
        self.chkBox_autoTest.setChecked(True)

        self.chkBoxLayout.addWidget(self.chkBox_autoTest)


        self.verticalLayout.addLayout(self.chkBoxLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.comboBox_threads.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u626b\u63cf\u8bbe\u7f6e", None))
        self.labMaxIP_1.setText(QCoreApplication.translate("Dialog", u"\u626b\u63cf\u51fa", None))
        self.labMaxIP_2.setText(QCoreApplication.translate("Dialog", u"\u6761IP\u540e\u505c\u6b62\u626b\u63cf", None))
        self.labThreads.setText(QCoreApplication.translate("Dialog", u"\u6700\u5927\u7ebf\u7a0b\u6570\uff1a", None))
        self.comboBox_threads.setItemText(0, QCoreApplication.translate("Dialog", u"1", None))
        self.comboBox_threads.setItemText(1, QCoreApplication.translate("Dialog", u"2", None))
        self.comboBox_threads.setItemText(2, QCoreApplication.translate("Dialog", u"4", None))
        self.comboBox_threads.setItemText(3, QCoreApplication.translate("Dialog", u"8", None))
        self.comboBox_threads.setItemText(4, QCoreApplication.translate("Dialog", u"16", None))
        self.comboBox_threads.setItemText(5, QCoreApplication.translate("Dialog", u"32", None))
        self.comboBox_threads.setItemText(6, QCoreApplication.translate("Dialog", u"64", None))
        self.comboBox_threads.setItemText(7, QCoreApplication.translate("Dialog", u"128", None))
        self.comboBox_threads.setItemText(8, QCoreApplication.translate("Dialog", u"200", None))

        self.chkBox_optimize.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528\u626b\u63cf\u4f18\u5316", None))
        self.chkBox_autoTest.setText(QCoreApplication.translate("Dialog", u"\u5b8c\u6210\u540e\u81ea\u52a8\u6d4b\u901f", None))
    # retranslateUi

