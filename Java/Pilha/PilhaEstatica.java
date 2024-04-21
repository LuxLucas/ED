<<<<<<< HEAD
public class PilhaEstatica{

    private String[] Pilha;
    private int UltimoIndice, Tamanho;

    public PilhaEstatica(int Tamanho){
        Pilha = new String[Tamanho];
        this.Tamanho = Tamanho;
        this.UltimoIndice = -1;
    }

    public int getTamanho(){
        return this.Pilha.length;
    }

    public boolean isVazio(){
        return this.getTamanho() == 0;
    }

    public boolean isCheio(){
        return this.getTamanho() == this.Tamanho;
    }

    public void empilharElemento(String Elemento){
        if(!this.isCheio()){
            this.UltimoIndice ++;
            this.Pilha[this.UltimoIndice] = Elemento;
        }
    }

    private String[] criarNovaPilha(int UltimoIndice){
        String[] NovaPilha = new String[this.Tamanho];
        for(int index = 0; index < this.Tamanho; index++){
            if(index != UltimoIndice){
                NovaPilha[index] = this.Pilha[index];
            }
        }
        return NovaPilha;
    }

    public String desempilharElemento(){
        String ElementoRemovido = null;
        if(!this.isVazio()){
            ElementoRemovido = this.Pilha[this.UltimoIndice];
            this.Pilha = this.criarNovaPilha(this.UltimoIndice);
            this.UltimoIndice--;
        }
        return ElementoRemovido;
    }
=======
public class PilhaEstatica{

    private String[] Pilha;
    private int UltimoIndice, Tamanho;

    public PilhaEstatica(int tamanho){
        Pilha = new String[tamanho];
        this.Tamanho = tamanho;
        this.UltimoIndice = -1;
    }

    public int getTamanho(){
        return this.Pilha.length;
    }

    public boolean isVazio(){
        return this.getTamanho() == 0;
    }

    public boolean isCheio(){
        return this.getTamanho() == this.Tamanho;
    }

    public void empilharElemento(String Elemento){
        if(!this.isCheio()){
            this.UltimoIndice ++;
            this.Pilha[this.UltimoIndice] = Elemento;
        }
    }

    private String[] criarNovaPilha(int UltimoIndice){
        String[] NovaPilha = new String[this.Tamanho];
        for(int index = 0; index < this.Tamanho; index++){
            if(index != UltimoIndice){
                NovaPilha[index] = this.Pilha[index];
            }
        }
        return NovaPilha;
    }

    public String desempilharElemento(){
        String ElementoRemovido = null;
        if(!this.isVazio()){
            ElementoRemovido = this.Pilha[this.UltimoIndice];
            this.Pilha = this.criarNovaPilha(this.UltimoIndice);
            this.UltimoIndice--;
        }
        return ElementoRemovido;
    }
>>>>>>> fbe8aacedfd0e9bde2aaf0c26a699d9fa5cbf0ca
}