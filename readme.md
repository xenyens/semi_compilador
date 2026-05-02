## Generar archivos con ANTLR4 - AUTOMATAS II

Desde la carpeta raíz `semi_compilador/`:

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener -o ../output grammar/Compilador.g4
```

Desde la carpeta `grammar/`:

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener -o ../output Compilador.g4
```
