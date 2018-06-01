#ifndef RECOMMENDATIONS_DIALOG_H
#define RECOMMENDATIONS_DIALOG_H

#include <QDialog>

namespace Ui {
class Recommendations_Dialog;
}

class Recommendations_Dialog : public QDialog
{
    Q_OBJECT

public:
    explicit Recommendations_Dialog(QWidget *parent = 0);
    ~Recommendations_Dialog();

private:
    Ui::Recommendations_Dialog *ui;
};

#endif // RECOMMENDATIONS_DIALOG_H
