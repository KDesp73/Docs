---
title: Room Api (Kotlin)
date: 2024-04-06 08:22:00 +0200
categories: [tutorial]
tags: [kotlin, android, room-api, db]
---

## Dependencies

### build.gradle.kts (root)

```kotlin
plugins {
  ...
  id("com.google.devtools.ksp") vesion "1.9.0-1.0.13" apply false
  ...
}
```
### build.gradle.kts (module)

```kotlin
plugins {
  ...
  id("com.google.devtools.ksp")
  ...
}

dependencies {
  val roomVersion = "2.6.1"
  implementation("androidx.room:room-runtime:$roomVersion")
  ksp("androidx.room:room-compiler:$roomVersion") // IMPORTANT

  implementation("androidx.room:room-ktx:$roomVersion")
  implementation("androidx.room:room-rxjava2:$roomVersion")
  implementation("androidx.room:room-rxjava3:$roomVersion")
  implementation("androidx.room:room-guava:$roomVersion")
  testImplementation("androidx.room:room-testing:$roomVersion")
  implementation("androidx.room:room-paging:$roomVersion")
}
```


## Database Abstract class

```kotlin
@Database(entities = arrayOf([Tables...]), version = 1, exportSchema = false)
abstract class MyDatabase : RoomDatabase() {
  abstract fun table1Dao(): Table1Dao

  abstract fun table2Dao(): Table2Dao
}
```

### Example

```kotlin
@Database(entities = arrayOf(User::class, Settings::class), version = 1, exportSchema = false)
abstract class MyDatabase : RoomDatabase() {
  abstract fun userDao(): UserDao

  abstract fun settingsDao(): SettingsDao
}
```

## Define a table / class

```kotlin
@Entity
data class User (
  @PrimaryKey var id: Int,
  @ColumnInfo(name = "email") var email: String,
  @ColumnInfo(name = "fname") var firstName: String,
  @ColumnInfo(name = "gender") var gender: String = "Other"
) {
  // .. other constructors / methods .. 
}
```

## Define the DAO (Data Access Object)

```kotlin
@Dao
interface UserDao {
  @Query("SELECT email FROM User")
  fun getEmails(): List<String>

  @Query("SELECT * FROM User WHERE id = :id")
  fun getUser(id: Int): User

  @Insert
  fun insert(vararg user: User)

  @Delete
  fun delete(user: User)
}
```

## Create a Database Object

```kotlin
val room = Room.databaseBuilder(
  applicationContext,
  MyDatabase::class.java,
  "local-db"
).allowMainThreadQueries() // To allow queries on the main thread
  .fallbackToDestructiveMigration() // Clear the database if no migration is defined
  .build()
```

## Usage

```kotlin
val userDao = room.userDao()
val emails = userDao.getEmails();

userDao.insertUser(User(...))
```
