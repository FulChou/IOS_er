package com.fulchou.Service;

import org.springframework.stereotype.Service;

import java.util.List;

@Service
public interface UserService {
    String getName();
    int getId();
    List<String> getHoppy();
}
