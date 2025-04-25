import requests
import flet as ft


def main(page: ft.Page):
  page.title = "Repositórios GitHub do Vitinho"
  page.theme_mode = ft.ThemeMode.DARK
  page.padding = 50
  page.update()

  page.appbar = ft.AppBar(
        title=ft.Text("Projetos DevFinOps"),
        center_title=True,
        bgcolor="#003020",
    )

  #Captura os dados que são exibidos como galeria
  repositories_data = get_github_public_repositories()
  gallery = []
  
  for content in repositories_data:
    gallery.append(ft.Container(
      content=ft.Text(content['name'], weight=ft.FontWeight.W_900, size=15, color=ft.Colors.WHITE),
      width=200,
      height=100,
      alignment=ft.alignment.center,
      bgcolor=ft.Colors.PURPLE_500,
      border_radius=5,
      padding=10,
      margin=5,
      border=ft.border.all(1, ft.Colors.BLACK12),
      shadow=ft.BoxShadow(blur_radius=3, color=ft.Colors.BLACK12),
      data=content['url'],
      on_click=lambda e: page.launch_url(e.control.data),
    ))

  page.add(
    ft.Row(
      controls=gallery,
      wrap=True,
      run_spacing=10,
      spacing=10,
      alignment=ft.MainAxisAlignment.CENTER,
    )
  )


def get_github_public_repositories():
    username = ""
    url = f"https://api.github.com/users/{username}/repos"
    token = ""
    header = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=header)
    list_repositories = []
    
    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            list_repositories.append({"name": repo['name'], 
                                      "url":repo['html_url']})
            
        return list_repositories
        
    else:
        print(f"Erro ao obter os repositórios: {response.status_code}")
        print(response.text)
        return []
    

if __name__ == "__main__":
  ft.app(target=main, port=8080)