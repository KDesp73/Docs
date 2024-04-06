---
title: Room Api (Kotlin)
date: 2024-04-06 08:22:00 +0200
categories: [tutorial]
tags: [kotlin, android, room-api, db]
---

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
