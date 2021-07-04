from main import Pessoas #, db_session

def insere_pessoas():
  pessoa = Pessoas(nome='Russo', idade=25)
  print(pessoa)
  pessoa.save()
#  db_session.add(pessoa)
#  db_session.commit()

def consulta():
  pessoa=Pessoas.query.all()
  print(pessoa)


  if __name__=='__main__':
    insere_pessoas()
    consulta()