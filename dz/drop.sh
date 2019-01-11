mysqldump -p12345678 --add-drop-table --no-data hw | grep -e '^DROP \| FOREIGN_KEY_CHECKS' | mysql -p12345678 hw
