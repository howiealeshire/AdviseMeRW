#include "recommendations_dialog.h"
#include "ui_recommendations_dialog.h"

Recommendations_Dialog::Recommendations_Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Recommendations_Dialog)
{
    ui->setupUi(this);
}

Recommendations_Dialog::~Recommendations_Dialog()
{
    delete ui;
}
