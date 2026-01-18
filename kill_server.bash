#!/bin/bash
echo "Matando procesos Python..."
pkill -9 python
sleep 1
echo "✓ Procesos detenidos"
echo ""
echo "Verificando puerto 5000..."
if netstat -an | grep -q 5000; then
    echo "⚠ Aún hay conexiones en puerto 5000"
else
    echo "✓ Puerto 5000 está libre"
fi