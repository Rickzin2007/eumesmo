usuario = {
    'nome' : 'Henrique',
    'idade' : 17,
    
}

print(type(usuario))
print(usuario)

print(f'Nome: {usuario["nome"]} ') 
print(f'Idade: {usuario["idade"]} ')

usuarios = ['leoanardo', 'henrique']
print(usuarios)
print(f'Nome: {usuarios[-2]} ')

print(f'Nome: {usuario.get('nome')} ') 