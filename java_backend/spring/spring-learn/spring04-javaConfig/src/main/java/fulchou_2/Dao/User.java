package fulchou_2.Dao;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Scope;

import java.util.List;

@Scope("Singleton")
public class User {
    @Value("fulchou_2_hhh")
    private String name;
    @Value("0931")
    private int id;
    private List<String> hoppy;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<String> getHoppy() {
        return hoppy;
    }

    public void setHoppy(List<String> hoppy) {
        this.hoppy = hoppy;
    }
}
