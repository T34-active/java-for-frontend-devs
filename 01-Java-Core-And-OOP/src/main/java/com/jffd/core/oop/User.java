package com.jffd.core.oop;

import java.util.Objects;

/**
 * 手写 equals/hashCode 的实体示例。
 * 生产中可用 Lombok @EqualsAndHashCode 或直接用 record（值对象）。
 */
public class User {

    private final Long id;
    private final String email;

    public User(Long id, String email) {
        this.id = Objects.requireNonNull(id, "id");
        this.email = Objects.requireNonNull(email, "email");
    }

    public Long getId() {
        return id;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof User user)) {
            return false;
        }
        // 业务上常以业务主键相等；这里用 id
        return Objects.equals(id, user.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    @Override
    public String toString() {
        return "User{id=" + id + ", email='" + email + "'}";
    }
}
