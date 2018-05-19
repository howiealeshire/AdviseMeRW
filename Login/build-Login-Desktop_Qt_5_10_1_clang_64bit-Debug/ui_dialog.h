/********************************************************************************
** Form generated from reading UI file 'dialog.ui'
**
** Created by: Qt User Interface Compiler version 5.10.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DIALOG_H
#define UI_DIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *username_horiz_layout;
    QLabel *username_lbl;
    QLineEdit *username_line_edit;
    QWidget *horizontalLayoutWidget_2;
    QHBoxLayout *password_horiz_layout;
    QLabel *password_lbl;
    QLineEdit *password_line_edit;
    QPushButton *register_btn;
    QPushButton *sign_in_btn;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QStringLiteral("Dialog"));
        Dialog->resize(262, 222);
        horizontalLayoutWidget = new QWidget(Dialog);
        horizontalLayoutWidget->setObjectName(QStringLiteral("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(10, 10, 181, 51));
        username_horiz_layout = new QHBoxLayout(horizontalLayoutWidget);
        username_horiz_layout->setSpacing(6);
        username_horiz_layout->setContentsMargins(11, 11, 11, 11);
        username_horiz_layout->setObjectName(QStringLiteral("username_horiz_layout"));
        username_horiz_layout->setContentsMargins(0, 0, 0, 0);
        username_lbl = new QLabel(horizontalLayoutWidget);
        username_lbl->setObjectName(QStringLiteral("username_lbl"));

        username_horiz_layout->addWidget(username_lbl);

        username_line_edit = new QLineEdit(horizontalLayoutWidget);
        username_line_edit->setObjectName(QStringLiteral("username_line_edit"));

        username_horiz_layout->addWidget(username_line_edit);

        horizontalLayoutWidget_2 = new QWidget(Dialog);
        horizontalLayoutWidget_2->setObjectName(QStringLiteral("horizontalLayoutWidget_2"));
        horizontalLayoutWidget_2->setGeometry(QRect(10, 80, 181, 41));
        password_horiz_layout = new QHBoxLayout(horizontalLayoutWidget_2);
        password_horiz_layout->setSpacing(6);
        password_horiz_layout->setContentsMargins(11, 11, 11, 11);
        password_horiz_layout->setObjectName(QStringLiteral("password_horiz_layout"));
        password_horiz_layout->setContentsMargins(0, 0, 0, 0);
        password_lbl = new QLabel(horizontalLayoutWidget_2);
        password_lbl->setObjectName(QStringLiteral("password_lbl"));

        password_horiz_layout->addWidget(password_lbl);

        password_line_edit = new QLineEdit(horizontalLayoutWidget_2);
        password_line_edit->setObjectName(QStringLiteral("password_line_edit"));

        password_horiz_layout->addWidget(password_line_edit);

        register_btn = new QPushButton(Dialog);
        register_btn->setObjectName(QStringLiteral("register_btn"));
        register_btn->setGeometry(QRect(130, 150, 113, 32));
        sign_in_btn = new QPushButton(Dialog);
        sign_in_btn->setObjectName(QStringLiteral("sign_in_btn"));
        sign_in_btn->setGeometry(QRect(10, 150, 113, 32));

        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", nullptr));
        username_lbl->setText(QApplication::translate("Dialog", "Username", nullptr));
        password_lbl->setText(QApplication::translate("Dialog", "Password", nullptr));
        register_btn->setText(QApplication::translate("Dialog", "Register", nullptr));
        sign_in_btn->setText(QApplication::translate("Dialog", "Sign In", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DIALOG_H
