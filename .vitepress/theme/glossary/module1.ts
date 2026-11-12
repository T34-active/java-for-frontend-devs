/**
 * 模块一术语表：id → 展示名 + 短释义（点按弹出）。
 * 释义用大白话，面向前端转 Java；详细展开仍回各章正文。
 */
export type GlossaryTerm = {
  id: string
  label: string
  def: string
  /** 可选：术语页锚点或章节相对链接 */
  more?: string
}

export const module1Glossary: GlossaryTerm[] = [
  {
    id: 'strong-typing',
    label: '强类型',
    def: '变量和表达式在编译期就有确定类型；类型对不上，编译器直接报错，而不是拖到运行时再「尽量帮你转」。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'primitive',
    label: '基本类型',
    def: 'Java 的 8 种纯值类型（如 int、boolean）。槽位里直接存值，不能为 null，也没有实例方法。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'reference-type',
    label: '引用类型',
    def: '变量里存的是「箭头」（引用），指向堆上的对象；可以为 null。String、数组、List、你自己写的类都属于这一族。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'wrapper',
    label: '包装类型',
    def: '把基本类型包成对象的类，如 Integer 对应 int。可以为 null，也能放进 List/Map；代价是多一层对象。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'boxing',
    label: '装箱',
    def: '基本类型 → 包装类型，例如 int 变成 Integer。常由编译器自动完成（自动装箱）。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'unboxing',
    label: '拆箱',
    def: '包装类型 → 基本类型，例如 Integer 变成 int。若包装引用是 null，拆箱会抛 NPE。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'npe',
    label: 'NPE',
    def: 'NullPointerException：对 null 引用调用方法、取字段或拆箱时抛出。后端日志里最常见的运行时异常之一。',
    more: '/01-Java-Core-And-OOP/06-exception-system',
  },
  {
    id: 'value-passing',
    label: '值传递',
    def: '方法收到的永远是实参的副本。传基本类型拷贝值；传对象拷贝「引用副本」。改对象字段外面看得见，重绑形参不影响调用方变量。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'equals',
    label: 'equals',
    def: '由类定义的「内容是否相等」。引用类型比内容时用 equals（或 Objects.equals），不要默认用 ==。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'double-equals',
    label: '==',
    def: '对基本类型比数值；对引用类型比「是不是同一个对象」（同一条箭头）。业务内容比较优先用 equals。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'final',
    label: 'final',
    def: '修饰变量时表示「不能再换绑」：基本类型值不能改；引用类型箭头不能换，但对象内部仍可能可变（如 final List 还能 add）。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'optional',
    label: 'Optional',
    def: '用「有值 / 空盒子」显式表达返回值可能没有。适合方法返回值边界，不适合当实体字段到处传。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'bigdecimal',
    label: 'BigDecimal',
    def: '精确十进制数值类型。金额、费率用它；用字符串构造（new BigDecimal("0.1")），避免 double 的二进制误差。',
    more: '/01-Java-Core-And-OOP/01-strong-typing-and-basics',
  },
  {
    id: 'encapsulation',
    label: '封装',
    def: '把对象内部数据藏起来，只通过受控方法对外交互。字段常 private，避免外面随便改坏不变量。',
    more: '/01-Java-Core-And-OOP/02-oop-deep-dive',
  },
  {
    id: 'composition',
    label: '组合',
    def: 'A「拥有」一个 B（has-a），用字段持有依赖。复用行为优先「接口 + 组合」，而不是深继承。',
    more: '/01-Java-Core-And-OOP/02-oop-deep-dive',
  },
  {
    id: 'inheritance',
    label: '继承',
    def: 'A「是一种」B（is-a），用 extends。Java 单继承；树宜浅，深继承容易出现脆弱基类问题。',
    more: '/01-Java-Core-And-OOP/02-oop-deep-dive',
  },
  {
    id: 'polymorphism',
    label: '多态',
    def: '用父类型/接口变量指向子类型对象：编译期按左边类型检查，运行期按右边实际对象执行实现。',
    more: '/01-Java-Core-And-OOP/02-oop-deep-dive',
  },
  {
    id: 'hashcode-contract',
    label: 'equals/hashCode 契约',
    def: '若 equals 为 true，hashCode 必须相等；否则放进 HashMap/HashSet 可能找不到。参与二者的字段放入集合后不要再改。',
    more: '/01-Java-Core-And-OOP/02-oop-deep-dive',
  },
  {
    id: 'record',
    label: 'record',
    def: '不可变数据载体的简写类。编译器生成构造器、访问器、equals、hashCode、toString。',
    more: '/01-Java-Core-And-OOP/02-oop-deep-dive',
  },
  {
    id: 'arraylist',
    label: 'ArrayList',
    def: '最常用的 List 实现：底层可扩容数组。尾部添加快，中间插入/删除要搬元素；随机下标访问 O(1)。',
    more: '/01-Java-Core-And-OOP/03-collections-framework',
  },
  {
    id: 'hashmap',
    label: 'HashMap',
    def: '最常用的 Map：hash → 桶 → equals 比键。默认负载因子 0.75；桶内过长可能树化。不是线程安全的。',
    more: '/01-Java-Core-And-OOP/03-collections-framework',
  },
  {
    id: 'fail-fast',
    label: 'fail-fast',
    def: '遍历时若集合结构被意外修改，尽快抛 ConcurrentModificationException，避免静默错乱。单线程增强 for 里直接 remove 也会触发。',
    more: '/01-Java-Core-And-OOP/03-collections-framework',
  },
  {
    id: 'cme',
    label: 'CME',
    def: 'ConcurrentModificationException：fail-fast 集合在迭代期间发生结构性修改时抛出。正确删除用 removeIf 或迭代器自己的 remove。',
    more: '/01-Java-Core-And-OOP/03-collections-framework',
  },
  {
    id: 'generics',
    label: '泛型',
    def: '用类型参数（如 List<String>）在编译期约束集合/方法里装什么，少做强制转换，把类型错误提前到编译期。',
    more: '/01-Java-Core-And-OOP/04-generics',
  },
  {
    id: 'type-erasure',
    label: '类型擦除',
    def: '泛型主要在编译期检查；编译后类型参数基本消失，运行时多为原始类型。因此不能 new T()、不能 List<int>。',
    more: '/01-Java-Core-And-OOP/04-generics',
  },
  {
    id: 'pecs',
    label: 'PECS',
    def: 'Producer Extends, Consumer Super：只读生产者用 ? extends；只写消费者用 ? super。用来在不变泛型上打开有限的读/写灵活度。',
    more: '/01-Java-Core-And-OOP/04-generics',
  },
  {
    id: 'wildcard',
    label: '通配符',
    def: '泛型里的 ?、? extends T、? super T。表示「某种未知类型」，用来表达只读或只写场景，而不是随意当子类型赋值。',
    more: '/01-Java-Core-And-OOP/04-generics',
  },
  {
    id: 'lambda',
    label: 'Lambda',
    def: '可传递的简短行为表达式，必须匹配某个函数式接口（只有一个抽象方法的接口）。',
    more: '/01-Java-Core-And-OOP/05-stream-and-lambda',
  },
  {
    id: 'stream',
    label: 'Stream',
    def: '一次性数据处理管道：先声明过滤/映射等中间操作（惰性），终端操作才真正计算。用过即废，不能反复复用。',
    more: '/01-Java-Core-And-OOP/05-stream-and-lambda',
  },
  {
    id: 'lazy',
    label: '惰性求值',
    def: '中间操作只登记「打算怎么做」，遇到终端操作才开算。因此 findFirst 等可以短路，不必扫完全表。',
    more: '/01-Java-Core-And-OOP/05-stream-and-lambda',
  },
  {
    id: 'checked-exception',
    label: '受检异常',
    def: '编译器强制你 catch 或在方法上 throws 的 Exception（非 RuntimeException）。想逼你正视可能失败的 IO/SQL 等；业务失败多用运行时异常。',
    more: '/01-Java-Core-And-OOP/06-exception-system',
  },
  {
    id: 'unchecked-exception',
    label: '非受检异常',
    def: 'RuntimeException 及其子类；编译器不强制处理。NPE、自定义 BizException 通常走这条。',
    more: '/01-Java-Core-And-OOP/06-exception-system',
  },
  {
    id: 'cause',
    label: 'cause',
    def: '异常的「根因」链。包装业务异常时要把底层异常传入构造器，排障才能顺着栈找到真正出错点。',
    more: '/01-Java-Core-And-OOP/06-exception-system',
  },
  {
    id: 'twr',
    label: 'try-with-resources',
    def: 'try (资源) { ... }：离开块时自动 close。资源需实现 AutoCloseable，比手写 finally 关流更不容易漏关或掩盖原异常。',
    more: '/01-Java-Core-And-OOP/06-exception-system',
  },
  {
    id: 'jdk',
    label: 'JDK',
    def: 'Java Development Kit：含编译器 javac、运行时 java 和标准库。本教程需要 JDK 17+，不要只装 JRE。',
    more: '/01-Java-Core-And-OOP/00-install-jdk-and-toolchain',
  },
  {
    id: 'jvm',
    label: 'JVM',
    def: 'Java Virtual Machine：执行字节码的虚拟机，包含在 JDK 里。你写的 .java 编译成 .class 后由它运行。',
    more: '/01-Java-Core-And-OOP/00-install-jdk-and-toolchain',
  },
  {
    id: 'maven',
    label: 'Maven',
    def: 'Java 生态常见的构建与依赖工具，读 pom.xml，类似前端的 npm/pnpm：下载依赖、编译、跑主类。',
    more: '/01-Java-Core-And-OOP/00-install-jdk-and-toolchain',
  },
]

export const module1ById: Record<string, GlossaryTerm> = Object.fromEntries(
  module1Glossary.map((t) => [t.id, t]),
)
