

def main():
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
