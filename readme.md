# Simulador de RSDL

Esse simulador foi escrito visando compreender o funcionamento do escalonador proposto por Kolivas em 2007.
A base foi criada de acordo com as instruções originais https://ck.fandom.com/wiki/RSDL.
Mas a descrição assume um escalonador funcionando em um kernel ativo, então foi necessário preencher algumas lacunas para que o mesmo se comprota-se de forma didática. 

## Descrição geral

O programa simula uma CPU adicionando, solicitando e executando tarefas usando um escalonador RSDL.
Todo "clock" é exibido no output de forma a mostrar visualmente o estado das filas, tarefas e CPU no momento atual.
 O programa é iniciado em Rsdl_Sim.